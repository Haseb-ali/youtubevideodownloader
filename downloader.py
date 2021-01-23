from pytube import YouTube
from pytube.cli import  on_progress
from tkinter import *
from tkinter import ttk
import sys
import clipboard
from pytube.extract import video_info_url
app_window=Tk()
main_container=Frame(app_window)
app_convas=Canvas(main_container)   
vide_card_container=Frame(app_convas)
def app_window_desing():
    app_window.title("Youtube videos downloader")
    window_width=app_window.winfo_screenwidth()
    window_height=app_window.winfo_screenheight()
    app_window.geometry('%dx%d' %(window_width,window_height))
    app_window['background']='#f4f4f9'
    app_window.iconbitmap("icons/favicon.ico")
    main_container.pack(fill=BOTH,expand=1)
    app_convas.pack(side=LEFT,fill=BOTH,expand=1)
    app_scrollbal=ttk.Scrollbar(main_container,orient=VERTICAL,command=app_convas.yview)
    app_scrollbal.pack(side=RIGHT,fill=Y)
    app_convas.configure(yscrollcommand=app_scrollbal.set)
    app_convas.bind('<Configure>',lambda e:app_convas.configure(scrollregion=app_convas.bbox('all')))
    app_convas.create_window((0,0),window=vide_card_container,anchor="nw")
def video_card():
    video_url=clipboard.paste()
    #video_url=downlaod_video(video_url)
    video_card_frame=Frame(vide_card_container,bg="white",width=app_window.winfo_width()-60,height=80)
    video_title=Label(video_card_frame,text="Adding a Full Screen ScrollBar - Python Tkinter GUI Tutorial #96")
    video_lenght=Label(video_card_frame,text="Video lenght=3:00:25")
    video_title.place(x=10,y=12)
    video_lenght.place(x=1180,y=10)
    video_card_frame.pack(pady=16)
def app_header_componets():
    window_width=app_window.winfo_screenwidth()
    def download_video():
        video_card()
    header_container=Frame(vide_card_container,bg="#9bc1bc",width=app_window.winfo_width(),height=60)
    video_url=Button(header_container,text="paste link",bg="#1985a1",bd=0.5,activebackground='#1985a1' ,activeforeground="white",fg="white",font=('calibri bold',12),highlightcolor='red',height=2,command=download_video)
    video_url.place(x=12,y=6)
    header_container.pack()
def load_dowload_gui():
    app_window_desing()
    app_header_componets()
    app_window.mainloop()
def downlaod_video(video_url):
    try:
                #video_url=input("Enter youtube video url: = ")
                #yt=YouTube(video_url,on_progress_callback=on_progress)
                yt=YouTube(video_url)
                return yt.title
                # print(yt.title,"Downloading......")
                # print("video lenght :",yt.length,'Seconds')
                # yt.streams.filter(progressive=True,file_extension='mp4').order_by("resolution").desc().first().download()
                # print(yt.title,"downloading completed...")
    except:
            print("Error:= ",sys.exc_info())
load_dowload_gui()