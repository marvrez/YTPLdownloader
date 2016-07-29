from progress_bar import progress_bar
from pytube import YouTube
import time
import sys
import re
import os
import requests
#TODO: implement this for playlists too

def download_video(url, folder):
    try:
        yt = YouTube(url)

    except Exception as e:
        print ("Error:", e.reason, "- skipping video with url:",url)
        return

    #video should be downloaded in 720p
    try:
        vid = yt.get("mp4","720p")

    #else tries to get the highest resolution available
    except Exception:
        vid = yt.filter("mp4")[-1]

    #download video
    try:
        bar = progress_bar()#init progress_bar
        vid.download(folder,on_progress = bar.print_progress, on_finish = bar.print_end)
        print("Successfully downloaded", yt.filename, " !")

    except OSError:
        print(yt.filename, "already exists in the directory. Skipping video...")
    
    #converts video to audio
    #TODO: try converting to WAV before MP3?
    try:
        aud = "ffmpeg -i "+str(yt.filename) + ".mp4 " + str(yt.filename)+".mp3"
        os.system(aud)
        print("Succesfully converted",yt.filename, "to mp3!")
    except OSError:
        print("There are some problems with the file name(s)..")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3: #usage #usage
        print("USAGE: python pl_downloader.py playlistURL OR python pl_downloader.py songFolder" )
        exit(1)

    else:
        url = sys.argv[1]

        if "https://" not in url:
            url = "https://%s" % (url)

        folder = os.getcwd() if len(sys.argv) != 3 else sys.argv[2] 
        #Creates a dir if it doesn't already exist
        try:
            os.makedirs(folder,exist_ok = True)
        except OSError as e:
            print (e)
            exit(1)

        download_video(url, folder)

