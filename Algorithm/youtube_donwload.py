from pytube import YouTube
import pytube.innertube

# Patch: force WEB client
pytube.innertube._default_clients["ANDROID"] = pytube.innertube._default_clients["WEB"]

link = input("Enter YouTube URL: ")
yt = YouTube(link)

print("Title:", yt.title)
stream = yt.streams.get_highest_resolution()
stream.download("downloads")
print("✅ Done!")
