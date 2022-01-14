# Youtube Downloader

## 1. Installation

1. You need to download the code from github [click here](https://github.com/CDKaisokuvn/ytb-download.git)
2. You need install python libraries by opening your command line and  using the following command:
 `pip install pytube tqdm typer rich`
3. add to PATH `set PATH=%PATH%;C:\your\path\here\` by example `set PATH=%PATH%;C:\duong\download\ytb-download\`. This allows you to execute the tool everywhere you need. Then done!!!

## 2. Usage
* To download a playlist:
  1. Copy the url of the playlist.
  2. Open the command line then move in where you want to download the playlist. This is an option, if you don't know how, dont worry.
  3. Write in the command line `ytbdl list "url of playlist" "destination"`. Here, destination can be a folder name if you have done the step 2. If the folder do not exist, it will be created automatically. If not, you can use a path line "C:\Users\duong\Desktop\Ship".
  4. Enter and wait a few seconds.
* To download a video: You have just change `list` by `single`
