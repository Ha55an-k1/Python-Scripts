import sys
from youtube_dl import YoutubeDL
import youtube_dl.postprocessor.ffmpeg
"""
Requires youtube_dl module and ffmpeg/avconv libraries
Youtube_DL--https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
FFMPEG--https://ffmpeg.org/download.html
->Keep youtube_dl updated
>pip install -U youtube-dl
"""


video_url=sys.argv[1:]
prompt='''
-------------------
|Confirm Download!|
-------------------
    ----------
    |Yes   No|
    ----------
'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ans=input(prompt)
        if ans.lower()=='yes':
            #set format for audio file
            ydl_opts = 
            {
            'format':'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }]
            }

            ydl = YoutubeDL(ydl_opts)
            ydl.download(video_url)
        else:
            print('Download Aborted!')
    else:
        print("Enter list of urls to download")
        exit(0)
