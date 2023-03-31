"""
download from youtube
"""

import os
from pytube import YouTube
from moviepy.editor import *

def create_directory(directory_name):
    """Create a new directory if not
    already existing
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print(f"{directory_name} already exists")

def download_audio(url, pfad = "audio_files"):
    """Download selected url
    """
    create_directory(pfad)
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download()
    audio = AudioFileClip(audio_file)
    mp3_file = os.path.splitext(os.path.basename(audio_file))[0] + ".mp3"
    mp3_path = os.path.join("audio_files", mp3_file)
    audio.write_audiofile(mp3_path)
    os.remove(audio_file)
    print(f"Audio downloaded successfully and saved as {mp3_file} in the audio_files directory.")
    return mp3_path

if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=MbiSd-4Zxps")

