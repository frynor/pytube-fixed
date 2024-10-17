from pytubefix import YouTube
import os

def download_youtube_video(url, output_path='./'):
    try:
     
        yt = YouTube(url)

    
        video = yt.streams.get_highest_resolution()


        title = ''.join(c for c in yt.title if c.isalnum() or c in (' ', '-', '_')).rstrip()

        # Download the video
        print(f"Downloading: {title}")
        video.download(output_path=output_path, filename=f"{title}.mp4")
        print(f"Download complete: {os.path.join(output_path, title)}.mp4")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
