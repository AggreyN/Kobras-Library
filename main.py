from mutagen.mp3 import MP3 # used to read mp3 files
from mutagen.easyid3 import EasyID3 # used to read mp3 metadata
from mutagen.easymp4 import EasyMP4 # 
from mutagen import File # used to read different file types

import pandas as pd 
import numpy as np 
import os # lets me interact with the operating system

import sys 
import importlib # used to import modules in runtime
import glob
import pprint

prefix = "C:\\Users\\aggre\\OneDrive\\Documents\\Coding Projects\\Kobras-Library\\MusicExamples\\"


#pulling from a file and displaying the tags

mp3_file = EasyID3(prefix + 'Halfcrazy.mp3')
print("MP3 Tags:")
pprint.pprint(mp3_file)
# Access specific tags:
print(f"Title: {mp3_file['title']}")
print(f"Artist: {mp3_file['artist']}")


class MusicFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.metadata = self._read_metadata()
        self.duration = self._read_duration()



def hi():
    music_folder = "C:\\Users\\aggre\\OneDrive\\Documents\\Coding Projects\\Kobras-Library\\MusicExamples"
    music_files = []

    # Walk through all subfolders
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            if file.endswith((".mp3", ".wav", ".m4a", ".flac")):
                full_path = os.path.join(root, file)
                music_files.append(file)

    print(f"Found {len(music_files)} music files")
    for file in music_files:
        print(file)
    print(music_files)

