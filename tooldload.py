from pytube import Playlist, YouTube
from tqdm import tqdm


def download_playlist(url, dest):
    p = Playlist(url)

    print("Downloading: " + p.title)
    for video in tqdm(p.videos):

        video.streams.filter(
            progressive=True,
            file_extension='mp4').order_by('resolution').last().download(dest)


def download_single(url, dest):
    v = YouTube(url)
    v.streams.filter(progressive=True,
                     file_extension='mp4').last().download(dest)
