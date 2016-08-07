from progress_bar import progress_bar
from PLparser     import parse
from pytube       import YouTube
import time
import sys
import re
import os
import requests
#TODO: fix decoding from utf-8


def download_video(url, folder):
    try:
        yt = YouTube(url)

    except Exception as e:
        print ("Error:", e, "- skipping video with url:",url)
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
        return
    
    #converts video to audio
    try:

            aud = "ffmpeg -i " + folder + "/" +  "\"" +  str(yt.filename) + "\"" + ".mp4 " + folder + "/" + "\""  + str(yt.filename) + "\"" + ".mp3"
            print (aud)
            os.system(aud)

            if os.path.exists(folder +"\\" + yt.filename + ".mp4"):
                os.remove(folder +"\\" + yt.filename + ".mp4")

            print("Succesfully converted",yt.filename, "to mp3!")

    except OSError:
        print("There are some problems with the file name(s), skipping video..")
        return


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3: #usage #usage
        print("USAGE: python pl_downloader.py URL OR python pl_downloader.py URL songFolder" )
        exit(1)

    else:
        url = sys.argv[1]

        if not url.startswith("https://"):
            url = "https://%s" % (url)

        folder = os.getcwd() if len(sys.argv) != 3 else sys.argv[2] 
        #Creates a dir if it doesn't already exist
        try:
            os.makedirs(folder,exist_ok = True)
        except OSError as e:
            print (e)
            exit(1)
        #if the given URL is of type youtube-playlist
        if "playlist?" in url:
            try:
                urls = parse(url)

            except Exception as e:
                print(e.reason)

            if urls:
                for url in urls:
                    download_video(url,folder)
            print("We did it reddit! 4Head")
        else:
            download_video(url, folder)
            print("We did it reddit! 4Head")

