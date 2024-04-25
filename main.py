import os
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        filename = stream.default_filename
        stream.download()
        print("Download completed successfully!")
        return filename
    except Exception as e:
        print("An error occurred:", str(e))

def download_videos_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()  # Remove leading/trailing whitespace
                if url:
                    download_video(url)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Download a single video")
    print("2. Download from a list")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        video_url = input("Enter the YouTube video URL: ")
        download_video(video_url)
    elif choice == "2":
        file_path = input("Enter the path to the file containing YouTube video URLs: ")
        download_videos_from_file(file_path)
    else:
        print("Invalid choice. Please choose 1 or 2.")
