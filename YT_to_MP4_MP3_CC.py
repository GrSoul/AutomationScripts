# YouTube downloader to MP4, MP3, captions

from pytube import YouTube

def Download(link, file_format, resolution=None):
    youtubeObject = YouTube(link)
    if file_format == 'mp4':
        if resolution:
            youtubeObject = youtubeObject.streams.filter(file_extension='mp4', resolution=resolution).first()
        else:
            youtubeObject = youtubeObject.streams.filter(file_extension='mp4').get_highest_resolution()
    elif file_format == 'mp3':
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    elif file_format == 'cc':
        caption = youtubeObject.captions.get_by_language_code('en')
        if caption:
            with open(f"{youtubeObject.title}.txt", "w") as f:
                f.write(caption.generate_srt_captions())
            print("CC downloaded successfully")
            return
        else:
            print("CC not available")
            return
    else:
        print("Invalid format. Please choose either 'mp4', 'mp3' or 'cc'.")
        return
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
file_format = input("Enter the desired file format (mp4, mp3 or cc): ")
if file_format == 'mp4':
    resolution = input("Enter the desired resolution (e.g. 720p, 1080p) or leave blank for highest available: ")
else:
    resolution = None
Download(link, file_format, resolution)