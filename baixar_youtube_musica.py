from pytube import YouTube
import os


def ask_to_user():
    link = str(input("Digite a URL do vídeo que será extraído o áudio: "))
    return YouTube(link)


def extract_audio(url):
    return url.streams.filter(only_audio=True).first()


def download_audio(url):
    audio = extract_audio(url)

    out_file = audio.download('musicas_python')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(url.title + ' audio has been sucessfully downloaded')


if __name__ == '__main__':
    try:
        url = ask_to_user()
        download_audio(url)

    except:
        raise ValueError("Input a valid URL... If the issue persist, try another link.")
