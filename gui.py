from tkinter import *
from pytube import YouTube
from moviepy.editor import VideoFileClip

# https://youtu.be/A5njg_yeybY
root = Tk()
# Title
root.title("Youtube Video Downloader")
# To Set The Height and Width 400 from x-axis and 50 from y-axis
root.geometry('450x550+400+50')
# Disable Resiization
root.resizable(False,False)
# Download function
def download():
    v_link = Link.get('1.0','end')

# Download
    yt = YouTube(v_link) 
    # title = yt.title
    # Label(frame,text=title,fg='#57a1f8',bg='#F8EBE7', font=('Microsoft yahie UI Light',14,'bold')).place(x=10,y=300)
    root.title("Downloading")
    stream = yt.streams.filter(progressive=True, res=720)
    video = stream.first().download()
    root.title("Successfully Downloaded")
    clip = VideoFileClip(video)
    clip.close()
    # pass


# Background Color Change
root.configure(bg='#845EC2')
# To add image
img = PhotoImage(file='yticon.png')
# Label like a block in which we pass our image data
Label(image=img ,bd=1,bg='#845EC2').place(x=150,y=2)
# Size of the fram and bg color
frame = Frame(root,width=400, height=370,bg='#B39CD0')
# Location of the frame
frame.place(x=25,y=170)
# Input Field In Frame
heading =Label(frame,text='YouTube Video Downloder',fg='#57a1f8' ,bg='#F8EBE7', font=('Microsoft yahie UI Light',22,'bold'))
heading.place(x=10,y=10)

# Passing/Showing text in the frame
Label(frame,text="Link :->",fg='#57a1f8',bg='#F8EBE7', font=('Microsoft yahie UI Light',14,'bold')).place(x=10,y=80)


# Taking Link
Link = Text(frame, fg='black', bd=1, height=1, width=30,bg = "light yellow",font=('Microsoft yahie UI Light',13))
Link.place(x=95,y=83)

# Download Button 
Button(frame,width=10,padx=1,pady=3,text='Download',bg='#845EC2',fg='white', border=2, command=download, font=('Microsoft yahie UI Light',14,'bold')).place(x=140,y=200)
root.mainloop()