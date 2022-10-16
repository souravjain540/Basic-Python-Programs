from tkinter import *
import pyperclip
import pyshorteners

root = Tk()
root.geometry("365x503")
root.minsize(600, 500)
root.maxsize(600, 500)
root.title("URL Converter")

def Convert():
    label.pack_forget()
    url_type = clicked.get()
    s = pyshorteners.Shortener()
    if url_type == "chilpit":
        Short_link = s.chilpit.short(link.get())
    elif url_type == "clckru":
        Short_link = s.clckru.short(link.get())
    elif url_type == "dagd":
        Short_link = s.dagd.short(link.get())
    elif url_type == "osdb":
        Short_link = s.osdb.short(link.get())
    else:
        Short_link = s.tinyurl.short(link.get())

    short_link.set(Short_link)

def Copy():
    pyperclip.copy(short_link.get())
    label.pack()
    
options = [
	"chilpit",
	"clckru",
	"dagd",
	"osdb",
	"tinyurl"
]

Label(root,text="URL_SHORTNER",font=("Arial", 30)).pack(padx=50, pady=(40,10))


link = StringVar()
short_link = StringVar()
clicked = StringVar()
clicked.set( "tinyurl" )

Label(text="Enter Long URL").pack(pady=(50,0))

frame1 = Frame()
frame1.pack(fill=X,pady=(0,50))
URL = Entry(frame1,textvar=link,width=40,font=50)
URL.pack(side=LEFT,padx=(30,0))

drop = OptionMenu( frame1 , clicked , *options )
drop.pack(side=LEFT)

frame = Frame()
frame.pack(fill=X)

Label(frame, text="Get Short URL").pack(pady=(0,0))
Short = Entry(frame,textvar=short_link,width=20,font="20")
Short.pack(padx=(150,0),side=LEFT)

Copy_Btn = Button(frame,text="Copy URL",bg="deep sky blue",command=Copy)
Copy_Btn.pack(padx=(0,5),side=LEFT)

Convert_btn = Button(root,text="Convert URL" ,font="30",bg="deep sky blue",command=Convert)
Convert_btn.pack(pady=(50,0))

label = Label(root,text="Copied",bg="red")

root.mainloop()