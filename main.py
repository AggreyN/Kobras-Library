import os # lets me interact with the operating system
import mutagen #used for music file metadata
import pandas as pd # type: ignore # used for data manipulation and analysis
import numpy as np # type: ignore
import sys 

import importlib # used to import modules in runtime

music_folder = "C:\\Users\\aggre\\OneDrive\\Documents\\Coding Projects\\Kobras-Library\\MusicExamples"
music_files = []

# Walk through all subfolders
for root, dirs, files in os.walk(music_folder):
    for file in files:
        if file.endswith((".mp3", ".wav", ".m4a", ".flac")):
            full_path = os.path.join(root, file)
            music_files.append(full_path)

print(f"Found {len(music_files)} music files")
for file in music_files:
    print(file)