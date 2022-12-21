from pytube import YouTube
import os


def ask_to_user():
    link = str(input("Digite a URL do vídeo que será extraído o áudio: "))
    return YouTube(link)


def extract_audio(url):
    return url.streams.filter(only_audio=True).first()


def download_audio():
    url = ask_to_user()
    audio = extract_audio(url)

    print('Downloading {}.'.format(url.title))
    out_file = audio.download('musicas_python')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(url.title + ' audio has been sucessfully downloaded')


def download_video(video):
    print('Downloading {}.'.format(video.title))
    video.download('videos_python')
    print(video.title + ' audio has been sucessfully downloaded')


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


if __name__ == '__main__':
    try:
        request = int(input(
            """Choose which one to download:
    1 - .mp3
    2 - .mp4 low data consumption (144p)
    3 - .mp4 low data consumption (360p)
    4 - .mp4 high quality (720p)
Response: """
        ))

        if request == 1:
            download_audio()
        elif request == 2:
            download_low_quality_video()
        elif request == 3:
            download_medium_quality_video()
        elif request == 4:
            download_high_quality_video()
        else:
            raise ValueError('Invalid request!!!')

    except:
        raise ValueError("Input a valid URL... If the issue persist, try another link.")
