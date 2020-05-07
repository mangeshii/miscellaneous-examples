from pytube import YouTube


SAVE_PATH = "/home/mayur/Desktop/mangeshi/python/PythonAppVenv"

yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')

stream = yt.streams.first()

stream.download(SAVE_PATH)
