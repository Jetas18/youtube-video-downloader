from pytube import YouTube

# YouTube video URL
url = input( "youtube link to download? \n>")

download_path = "/home/jetas/Music"

yt = YouTube(url)
file = input("would you like just the audio or the video too?\n>")

if file == "video":
    stream = yt.streams.get_highest_resolution()
    download_path = "/home/jetas/Videos"
    stream.download(download_path)
    
    print("Video and audio downloaded successfully!")
elif file == "audio":
    audio = yt.streams.get_audio_only()
    audio.download(download_path)
else:
    print("invalid response")
    print("\n type-")
    print("\n audio: audio only download")
    print("\n video: for both audio and video")
