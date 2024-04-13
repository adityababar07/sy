from pytube import Playlist
from pytube import YouTube
import os

URL_PLAYLIST = "https://www.youtube.com/playlist?list=PLYwtShM4uUVnE8HLqpuucIkA7lEjyeejA"

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)

# print(urls)


for link in urls:
    yt=YouTube(link)
    # t=yt.streams.filter(only_audio=True).all()
    # t=yt.streams.get_audio_only()
    YTAUDIO_FILE_PATH = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download("/home/aditya/Music/")
    print(YTAUDIO_FILE_PATH)
    
    os.system(f"ffmpeg -i '{YTAUDIO_FILE_PATH}' -vn -ar 44100 -ac 2 -ab 192k -f mp3 '{YTAUDIO_FILE_PATH[:-4]}.mp3' && rm '{YTAUDIO_FILE_PATH}'")
    

    # t[0].download("/home/aditya/Music/")