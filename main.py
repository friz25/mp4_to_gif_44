# pip install ffmpeg-python
import ffmpeg


def video_to_gif():
    stream = ffmpeg.input("2.mp4")
    stream = ffmpeg.output(stream, "2.gif")
    ffmpeg.run(stream)


def main():
    video_to_gif()


if __name__ == '__main__':
    main()
