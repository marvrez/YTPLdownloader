import re
import urllib.error
import urllib.request
import sys
import time 
import os
#another branch of PLparser that instead of saving the URLs into a file
#parse now returns a list
def parse(url):
    final_url = []
    all_urls = []
    start = time.time()
    if ("list=" in url):
        eq = url.rfind("=")+1
        pl_code = url[eq:]

    else:
        print("Incorrect playlist, please try again with a correct Youtube playlist URL!")
        exit(1)
    try:
        yt_page = str(urllib.request.urlopen(url).read())

    except urllib.error.URLError as e:
        print (e.reason)

    pattern = re.compile(r"watch\?v=\S+?list=%s" % (pl_code) )
    match = re.findall(pattern,yt_page)

    if match:
        for __video in match:
            video = str(__video)
            if "&" in video:
                amp = video.index("&") 
                video_url = video[:amp]
                final_url.append("https://youtube.com/%s\n" % (video_url[:amp]))
        all_urls = list(set(final_url))
        print ("Elapsed time: %f" % (time.time()-start)) 
        print ("Done!", len(all_urls), "URLs parsed")
        return all_urls

    else:
        print ("No videos found in playlist")
        exit(1)

