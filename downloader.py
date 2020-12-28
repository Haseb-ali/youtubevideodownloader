from pytube import YouTube
from pytube.cli import  on_progress
import sys
while(True):
    try:
            video_url=input("Enter youtube video url: = ")
            yt=YouTube(video_url,on_progress_callback=on_progress)
            print(yt.title,"Downloading......")
            print("video lenght :",yt.length,'Seconds')
            yt.streams.filter(progressive=True,file_extension='mp4').order_by("resolution").desc().first().download()
            print(yt.title,"downloading completed...")
    except:
        print("Error:= ",sys.exc_info())