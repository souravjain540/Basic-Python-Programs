import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class FileManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter File Manager")
        self.geometry("900x600")
        self.minsize(800, 500)
        
        # Current directory
        self.current_path = os.path.expanduser("~")
        
        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create toolbar
        self.create_toolbar()
        
        # Create path entry
        self.create_path_entry()
        
        # Create file browser
        self.create_file_browser()
        
        # Create status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Populate the file list
        self.populate_file_list()
        
        # Bind right-click menu
        self.create_context_menu()

    def create_toolbar(self):
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(side=tk.TOP, fill=tk.X, pady=(0, 5))
        
        # Back button
        self.back_btn = ttk.Button(toolbar, text="Back", command=self.go_back)
        self.back_btn.pack(side=tk.LEFT, padx=2)
        
        # Home button
        self.home_btn = ttk.Button(toolbar, text="Home", command=self.go_home)
        self.home_btn.pack(side=tk.LEFT, padx=2)
        
        # Refresh button
        self.refresh_btn = ttk.Button(toolbar, text="Refresh", command=self.refresh)
        self.refresh_btn.pack(side=tk.LEFT, padx=2)
        
        # New folder button
        self.new_folder_btn = ttk.Button(toolbar, text="New Folder", command=self.create_new_folder)
        self.new_folder_btn.pack(side=tk.LEFT, padx=2)

    def create_path_entry(self):
        path_frame = ttk.Frame(self.main_frame)
        path_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        path_label = ttk.Label(path_frame, text="Path:")
        path_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.path_var = tk.StringVar(value=self.current_path)
        self.path_entry = ttk.Entry(path_frame, textvariable=self.path_var)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.path_entry.bind("<Return>", self.navigate_to_path)
        
        go_btn = ttk.Button(path_frame, text="Go", command=self.navigate_to_path)
        go_btn.pack(side=tk.LEFT, padx=(5, 0))

    def create_file_browser(self):
        browser_frame = ttk.Frame(self.main_frame)
        browser_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Create Treeview
        columns = ('name', 'size', 'type', 'modified')
        self.tree = ttk.Treeview(browser_frame, columns=columns, show='headings')
        
        # Define headings
        self.tree.heading('name', text='Name')
        self.tree.heading('size', text='Size')
        self.tree.heading('type', text='Type')
        self.tree.heading('modified', text='Modified')
        
        # Define columns
        self.tree.column('name', width=300)
        self.tree.column('size', width=100)
        self.tree.column('type', width=100)
        self.tree.column('modified', width=150)
        
        # Add scrollbars
        vsb = ttk.Scrollbar(browser_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(browser_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Grid layout
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        
        browser_frame.grid_columnconfigure(0, weight=1)
        browser_frame.grid_rowconfigure(0, weight=1)
        
        # Bind double-click event
        self.tree.bind("<Double-1>", self.on_item_double_click)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Open", command=self.open_selected)
        self.context_menu.add_command(label="Copy", command=self.copy_selected)
        self.context_menu.add_command(label="Cut", command=self.cut_selected)
        self.context_menu.add_command(label="Paste", command=self.paste_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Delete", command=self.delete_selected)
        self.context_menu.add_command(label="Rename", command=self.rename_selected)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Properties", command=self.show_properties)
        
        self.tree.bind("<Button-3>", self.show_context_menu)
        
        # Clipboard variable for copy/cut operations
        self.clipboard = {"action": None, "path": None}

    def populate_file_list(self):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            # Get and sort directories and files
            items = os.listdir(self.current_path)
            dirs = []
            files = []
            
            for item in items:
                item_path = os.path.join(self.current_path, item)
                if os.path.isdir(item_path):
                    dirs.append(item)
                else:
                    files.append(item)
            
            # Sort alphabetically
            dirs.sort(key=str.lower)
            files.sort(key=str.lower)
            
            # Add parent directory entry if not at root
            if os.path.dirname(self.current_path) != self.current_path:
                self.tree.insert('', 'end', values=('..', '', 'Directory', ''), tags=('directory',))
            
            # Add directories
            for directory in dirs:
                full_path = os.path.join(self.current_path, directory)
                modified_time = self.get_modified_time(full_path)
                self.tree.insert('', 'end', values=(directory, '', 'Directory', modified_time), tags=('directory',))
            
            # Add files
            for file in files:
                full_path = os.path.join(self.current_path, file)
                size = self.get_size_format(os.path.getsize(full_path))
                file_type = self.get_file_type(file)
                modified_time = self.get_modified_time(full_path)
                self.tree.insert('', 'end', values=(file, size, file_type, modified_time), tags=('file',))
            
            # Update path entry and status bar
            self.path_var.set(self.current_path)
            item_count = len(dirs) + len(files)
            self.status_var.set(f"{item_count} items | {len(dirs)} directories, {len(files)} files")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not access directory: {str(e)}")
            self.go_back()

    def get_size_format(self, size_bytes):
        """Convert size in bytes to human-readable format"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 ** 2:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 ** 3:
            return f"{size_bytes / (1024 ** 2):.1f} MB"
        else:
            return f"{size_bytes / (1024 ** 3):.1f} GB"

    def get_file_type(self, filename):
        """Get file type from extension"""
        extension = os.path.splitext(filename)[1]
        if not extension:
            return "File"
        return extension[1:].upper() + " File"

    def get_modified_time(self, path):
        """Get last modified time of a file or directory"""
        try:
            mtime = os.path.getmtime(path)
            return self.format_timestamp(mtime)
        except:
            return ""

    def format_timestamp(self, timestamp):
        """Format timestamp to human-readable format"""
        import datetime
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def on_item_double_click(self, event):
        """Handle double-click on an item"""
        selected_item = self.tree.selection()[0]
        item_values = self.tree.item(selected_item, 'values')
        
        if not item_values:
            return
        
        item_name = item_values[0]
        
        # Handle parent directory (..)
        if item_name == '..':
            self.go_back()
            return
        
        item_path = os.path.join(self.current_path, item_name)
        
        if os.path.isdir(item_path):
            # It's a directory, navigate into it
            self.current_path = item_path
            self.populate_file_list()
        else:
            # It's a file, try to open it
            self.open_file(item_path)

    def open_file(self, file_path):
        """Open a file with the default application"""
        try:
            import platform
            import subprocess
            
            if platform.system() == 'Windows':
                os.startfile(file_path)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', file_path))
            else:  # Linux
                subprocess.call(('xdg-open', file_path))
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {str(e)}")

    def go_back(self):
        """Navigate to the parent directory"""
        parent_dir = os.path.dirname(self.current_path)
        if parent_dir != self.current_path:  # Not at root
            self.current_path = parent_dir
            self.populate_file_list()

    def go_home(self):
        """Navigate to the home directory"""
        self.current_path = os.path.expanduser("~")
        self.populate_file_list()

    def refresh(self):
        """Refresh the current directory"""
        self.populate_file_list()

    def navigate_to_path(self, event=None):
        """Navigate to the path entered in the path entry"""
        new_path = self.path_var.get()
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_path = new_path
            self.populate_file_list()
        else:
            messagebox.showerror("Error", "Invalid directory path")
            self.path_var.set(self.current_path)

    def create_new_folder(self):
        """Create a new folder in the current directory"""
        folder_name = tk.simpledialog.askstring("New Folder", "Enter folder name:")
        if folder_name:
            try:
                new_folder_path = os.path.join(self.current_path, folder_name)
                os.makedirs(new_folder_path)
                self.refresh()
            except Exception as e:
                messagebox.showerror("Error", f"Could not create folder: {str(e)}")

    def show_context_menu(self, event):
        """Show context menu on right-click"""
        # Select the item under cursor
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
        # Display context menu
        self.context_menu.post(event.x_root, event.y_root)

    def get_selected_path(self):
        """Get the full path of the selected item"""
        try:
            selected_item = self.tree.selection()[0]
            item_name = self.tree.item(selected_item, 'values')[0]
            
            if item_name == '..':
                return os.path.dirname(self.current_path)
                
            return os.path.join(self.current_path, item_name)
        except:
            return None

    def open_selected(self):
        """Open the selected item"""
        selected_path = self.get_selected_path()
        if selected_path:
            if os.path.isdir(selected_path):
                self.current_path = selected_path
                self.populate_file_list()
            else:
                self.open_file(selected_path)

    def copy_selected(self):
        """Copy the selected item to clipboard"""
        selected_path = self.get_selected_path()
        if selected_path:
            self.clipboard["action"] = "copy"
            self.clipboard["path"] = selected_path
            self.status_var.set(f"Selected item ready to copy: {os.path.basename(selected_path)}")

    def cut_selected(self):
        """Cut the selected item to clipboard"""
        selected_path = self.get_selected_path()
        if selected_path:
            self.clipboard["action"] = "cut"
            self.clipboard["path"] = selected_path
            self.status_var.set(f"Selected item ready to move: {os.path.basename(selected_path)}")

    def paste_item(self):
        """Paste the item from clipboard to current directory"""
        if not self.clipboard["path"] or not self.clipboard["action"]:
            messagebox.showinfo("Info", "Nothing to paste")
            return
            
        src_path = self.clipboard["path"]
        src_name = os.path.basename(src_path)
        dst_path = os.path.join(self.current_path, src_name)
        
        # Check if source still exists
        if not os.path.exists(src_path):
            messagebox.showerror("Error", "Source item no longer exists")
            self.clipboard = {"action": None, "path": None}
            return
            
        # Check for existing destination
        if os.path.exists(dst_path):
            overwrite = messagebox.askyesno("Confirm", f"{src_name} already exists. Overwrite?")
            if not overwrite:
                return
        
        try:
            if self.clipboard["action"] == "copy":
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                self.status_var.set(f"Copied: {src_name}")
            elif self.clipboard["action"] == "cut":
                shutil.move(src_path, dst_path)
                self.status_var.set(f"Moved: {src_name}")
                self.clipboard = {"action": None, "path": None}
            
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Operation failed: {str(e)}")

    def delete_selected(self):
        """Delete the selected item"""
        selected_path = self.get_selected_path()
        if not selected_path:
            return
            
        item_name = os.path.basename(selected_path)
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{item_name}'?")
        
        if confirm:
            try:
                if os.path.isdir(selected_path):
                    shutil.rmtree(selected_path)
                else:
                    os.remove(selected_path)
                self.status_var.set(f"Deleted: {item_name}")
                self.refresh()
            except Exception as e:
                messagebox.showerror("Error", f"Could not delete item: {str(e)}")

    def rename_selected(self):
        """Rename the selected item"""
        selected_path = self.get_selected_path()
        if not selected_path:
            return
            
        old_name = os.path.basename(selected_path)
        new_name = tk.simpledialog.askstring("Rename", "Enter new name:", initialvalue=old_name)
        
        if new_name and new_name != old_name:
            new_path = os.path.join(os.path.dirname(selected_path), new_name)
            
            try:
                os.rename(selected_path, new_path)
                self.status_var.set(f"Renamed: {old_name} to {new_name}")
                self.refresh()
            except Exception as e:
                messagebox.showerror("Error", f"Could not rename item: {str(e)}")

    def show_properties(self):
        """Show properties of the selected item"""
        selected_path = self.get_selected_path()
        if not selected_path:
            return
            
        try:
            name = os.path.basename(selected_path)
            location = os.path.dirname(selected_path)
            
            if os.path.isdir(selected_path):
                type_str = "Directory"
                size = self.get_directory_size(selected_path)
            else:
                type_str = self.get_file_type(name)
                size = os.path.getsize(selected_path)
                
            size_str = self.get_size_format(size)
            created = self.format_timestamp(os.path.getctime(selected_path))
            modified = self.format_timestamp(os.path.getmtime(selected_path))
            
            info = f"Name: {name}\n"
            info += f"Type: {type_str}\n"
            info += f"Location: {location}\n"
            info += f"Size: {size_str}\n"
            info += f"Created: {created}\n"
            info += f"Modified: {modified}"
            
            messagebox.showinfo("Properties", info)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not get properties: {str(e)}")

    def get_directory_size(self, path):
        """Get the size of a directory including all its contents"""
        total_size = 0
        
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # Skip symbolic links
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
        except:
            pass
            
        return total_size

if __name__ == "__main__":
    app = FileManager()
    app.mainloop()
