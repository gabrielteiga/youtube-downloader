from pytube import YouTube
from pytube.cli import on_progress
import os


def ask_to_user():
    link = str(input("Give me a valid URL: "))
    return YouTube(link, on_progress_callback=on_progress)


def extract_audio(url):
    return url.streams.filter(only_audio=True).first()


def download_audio():
    url = ask_to_user()
    audio = extract_audio(url)

    print('Downloading {}.'.format(url.title))
    out_file = audio.download('musics_python')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('\n' + url.title + ' audio has been sucessfully downloaded')


def download_video(video):
    print('Downloading {}.'.format(video.title))
    video.download('videos_python')

    print('\n' + video.title + ' video has been sucessfully downloaded')


def download_low_quality_video():
    url = ask_to_user()
    video = url.streams.get_lowest_resolution()
    download_video(video)


def download_medium_quality_video():
    url = ask_to_user()
    video = url.streams.get_by_resolution('360p')
    download_video(video)


def download_high_quality_video():
    url = ask_to_user()
    video = url.streams.get_highest_resolution()
    download_video(video)
