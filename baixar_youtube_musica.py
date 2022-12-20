# Devemos executar o programa no cmd: python nome_arquivo.py "www.youtube.com/link_para_analise"
# A biblioteca "sys" vai fazer com que ele seja executado
# from sys import argv
from pytube import YouTube
import os

try:

    # link = argv[1] Com o sys, pegamos direto do prompt de comando
    # URL do Youtube
    link = str(input("Digite a URL do vídeo que será extraído o áudio: "))
    yt = YouTube(link)

    # Extraindo apenas o audio
    yd = yt.streams.filter(only_audio=True).first()  # Dessa maneira o arquivo fica mais leve

    # Download do arquivo
    out_file = yd.download('musicas_python')

    # Salvando como .mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    # Fim
    print(yt.title + " has been sucessfully downloaded")

except:
    raise ValueError("Deu um problema no download, tente novamente com uma url valida...")
