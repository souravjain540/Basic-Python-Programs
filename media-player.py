import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pygame
import os
import vlc
from PIL import Image, ImageTk

class MultimediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multimedia Player")
        self.root.geometry("800x600")

        # Initialize pygame mixer for music
        try:
            pygame.mixer.init()
        except Exception as e:
            messagebox.showerror("Error", f"Pygame Mixer Init Failed: {e}")

        # Initialize VLC for video
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Create main notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Create tabs
        self.music_frame = ttk.Frame(self.notebook)
        self.video_frame = ttk.Frame(self.notebook)
        self.image_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.music_frame, text="Music")
        self.notebook.add(self.video_frame, text="Video")
        self.notebook.add(self.image_frame, text="Images")

        # Music Player Setup
        self.setup_music_player()

        # Video Player Setup
        self.setup_video_player()

        # Image Viewer Setup
        self.setup_image_viewer()

    def setup_music_player(self):
        self.playlist = []
        self.current_track = None
        
        self.music_listbox = tk.Listbox(self.music_frame, width=60)
        self.music_listbox.pack(pady=10)

        music_controls_frame = ttk.Frame(self.music_frame)
        music_controls_frame.pack(pady=10)

        ttk.Button(music_controls_frame, text="Add Songs", command=self.add_songs).pack(side=tk.LEFT, padx=5)
        ttk.Button(music_controls_frame, text="Add Folder", command=self.add_music_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(music_controls_frame, text="Play", command=self.play_music).pack(side=tk.LEFT, padx=5)
        ttk.Button(music_controls_frame, text="Pause", command=self.pause_music).pack(side=tk.LEFT, padx=5)
        ttk.Button(music_controls_frame, text="Stop", command=self.stop_music).pack(side=tk.LEFT, padx=5)
        ttk.Button(music_controls_frame, text="Clear Playlist", command=self.clear_playlist).pack(side=tk.LEFT, padx=5)

    def setup_video_player(self):
        self.video_canvas = tk.Canvas(self.video_frame, width=640, height=360)
        self.video_canvas.pack()

        video_controls_frame = ttk.Frame(self.video_frame)
        video_controls_frame.pack(pady=10)

        ttk.Button(video_controls_frame, text="Open Video", command=self.open_video).pack(side=tk.LEFT, padx=5)
        ttk.Button(video_controls_frame, text="Open Video Folder", command=self.open_video_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(video_controls_frame, text="Play", command=self.play_video).pack(side=tk.LEFT, padx=5)
        ttk.Button(video_controls_frame, text="Pause", command=self.pause_video).pack(side=tk.LEFT, padx=5)
        ttk.Button(video_controls_frame, text="Stop", command=self.stop_video).pack(side=tk.LEFT, padx=5)

        # List to store video files
        self.video_playlist = []
        self.current_video_index = 0

        # Listbox to show video playlist
        self.video_listbox = tk.Listbox(self.video_frame, width=60)
        self.video_listbox.pack(pady=10)

    def setup_image_viewer(self):
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(expand=True, fill='both')

        image_controls_frame = ttk.Frame(self.image_frame)
        image_controls_frame.pack(pady=10)

        ttk.Button(image_controls_frame, text="Open Image", command=self.open_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(image_controls_frame, text="Open Image Folder", command=self.open_image_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(image_controls_frame, text="Next", command=self.next_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(image_controls_frame, text="Previous", command=self.previous_image).pack(side=tk.LEFT, padx=5)

        self.image_paths = []
        self.current_image_index = 0

    def add_songs(self):
        songs = filedialog.askopenfilenames(
            title="Choose Music Files", 
            filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")]
        )
        for song in songs:
            self.playlist.append(song)
            self.music_listbox.insert(tk.END, os.path.basename(song))

    def add_music_folder(self):
        folder_path = filedialog.askdirectory(title="Choose Music Folder")
        if folder_path:
            # Find all MP3 files in the selected folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.lower().endswith('.mp3'):
                        full_path = os.path.join(root, file)
                        self.playlist.append(full_path)
                        self.music_listbox.insert(tk.END, file)

    def clear_playlist(self):
        self.playlist.clear()
        self.music_listbox.delete(0, tk.END)
        pygame.mixer.music.stop()

    def play_music(self):
        if self.music_listbox.curselection():
            index = self.music_listbox.curselection()[0]
            self.current_track = self.playlist[index]
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("Warning", "No song selected!")

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def open_video(self):
        video_path = filedialog.askopenfilename(
            title="Choose Video File", 
            filetypes=[("Video Files", "*.mp4 *.avi *.mkv"), ("All Files", "*.*")]
        )
        if video_path:
            self.video_playlist.append(video_path)
            self.video_listbox.insert(tk.END, os.path.basename(video_path))
            # If this is the first video, play it
            if len(self.video_playlist) == 1:
                self.play_video()

    def open_video_folder(self):
        folder_path = filedialog.askdirectory(title="Choose Video Folder")
        if folder_path:
            # Video file extensions to look for
            video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
            
            # Find all video files in the selected folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in video_extensions):
                        full_path = os.path.join(root, file)
                        self.video_playlist.append(full_path)
                        self.video_listbox.insert(tk.END, file)
            
            # If this is the first video, play it
            if len(self.video_playlist) == 1:
                self.play_video()

    def play_video(self):
        if self.video_listbox.curselection():
            index = self.video_listbox.curselection()[0]
            video_path = self.video_playlist[index]
            media = self.instance.media_new(video_path)
            self.player.set_media(media)
            if os.name == "nt":
                self.player.set_hwnd(self.video_canvas.winfo_id())
            else:
                self.player.set_xwindow(self.video_canvas.winfo_id())
            self.player.play()
        elif self.video_playlist:
            # If no selection but playlist exists, play the first video
            video_path = self.video_playlist[0]
            media = self.instance.media_new(video_path)
            self.player.set_media(media)
            if os.name == "nt":
                self.player.set_hwnd(self.video_canvas.winfo_id())
            else:
                self.player.set_xwindow(self.video_canvas.winfo_id())
            self.player.play()
        else:
            messagebox.showwarning("Warning", "No video selected!")

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def open_image(self):
        image_paths = filedialog.askopenfilenames(
            title="Choose Image Files", 
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All Files", "*.*")]
        )
        self.image_paths.extend(list(image_paths))
        self.current_image_index = len(self.image_paths) - 1
        if self.image_paths:
            self.display_image()

    def open_image_folder(self):
        folder_path = filedialog.askdirectory(title="Choose Image Folder")
        if folder_path:
            # Image file extensions to look for
            image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
            
            # Find all image files in the selected folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in image_extensions):
                        full_path = os.path.join(root, file)
                        self.image_paths.append(full_path)
            
            # Set current image to the last added image
            self.current_image_index = len(self.image_paths) - 1
            if self.image_paths:
                self.display_image()

    def display_image(self):
        if 0 <= self.current_image_index < len(self.image_paths):
            image_path = self.image_paths[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((700, 500))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def next_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.display_image()

    def previous_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.display_image()

def main():
    root = tk.Tk()
    ttk.Style().theme_use('clam')
    app = MultimediaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
