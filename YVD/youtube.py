from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url, save_path):
    try : 
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path=save_path)
        print(" The video has been downloaded successfully!")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder



if __name__ == '__main__':

    root = tk.Tk()
    root.withdraw()


    url = input("Enter the URL of the video you want to download: ")
    save_path = open_file_dialog()

    if save_path:
        print("Started downloading...")
        download(url, save_path)
        
    else:
        print("Invalid save location.")