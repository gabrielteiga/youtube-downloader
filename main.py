from downloader_manager import download_audio, download_low_quality_video
from downloader_manager import download_medium_quality_video, download_high_quality_video


def run():
    try:
        request = int(input(
            """Choose which one to download:
    1 - .mp3(audio)
    2 - .mp4(video) - low data consumption (144p)
    3 - .mp4(video) - medium quality (360p)
    4 - .mp4(video) - high quality (720p)
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


if __name__ == '__main__':
    run()
