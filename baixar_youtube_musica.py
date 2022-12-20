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

    out_file = audio.download('musicas_python')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(url.title + ' audio has been sucessfully downloaded')


def download_high_quality_video():
    print('Feature in progress...')


def download_low_quality_video():
    print('Feature in progress...')


if __name__ == '__main__':
    try:
        request = int(input(
            """Choose which one to download:
    1 - .mp3
    2 - .mp4 high quality
    3 - .mp4 low data consumption
Response: """
        ))

        if request == 1:
          download_audio()
        elif request == 2:
          download_high_quality_video()
        elif request == 3:
          download_low_quality_video()
        else:
          raise ValueError('Invalid request!!!')

    except:
        raise ValueError("Input a valid URL... If the issue persist, try another link.")