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





import tkinter as tk

def KobraGUI():
    display = tk.Tk() #this will create the display basically
    
    display.geometry("800x600") #setting up dimentions
    display.title("Kobras Library")
    
    label = tk.Label(display, text = "Welcome to Kobra's Library!!", font = ('Helvetica', 22))#creating a simple label for testing
    label.pack(padx=40, pady= 20)
    # the pack func tells python where to put the code, and the pads tell how far from the borders you want it.
    
    textbox = tk.Text(display, text = "Type Your Name: " height = 3, font = ('Helvetica', 15)) #a textbox
    textbox.pack(padx= 10)
    
    
    button = tk.Button(display, text = "Click for Menu!", font = ('Helvetica', 20))
    button.pack(padx = 10, pady = 10)
    display.mainloop() #this makes the display continue consistently Im pretty sure
    


KobraGUI()





prefix = "C:\\Users\\aggre\\OneDrive\\Documents\\Coding Projects\\Kobras-Library\\MusicExamples\\" #for simplicity purposes


#pulling from a file and displaying the tags

userfile = input("Enter the file name: ")
mp3_file = EasyID3(prefix + 'Halfcrazy.mp3')
print("MP3 Tags:")
pprint.pprint(mp3_file) #this is to have the files print out nice 



# Access specific tags:
print(f"Title: {mp3_file['title']}")
print(f"Artist: {mp3_file['artist']}")




class Kobralib():
    """
    Docstring for Kobralib   
    This class will display the main menu for the library where the use can choose from,
        - Adding a to the Library
        - Viewing Library
        - Deleting from the file
        - Viewing Genres
        - Exiting the menu
        * These are preliminary as for now VERY subject to change
    Attributes:
        Folderfile(str): the folder in which we will be pulling from (as of rn) for code
    """
    def __init__(self,folderfile,):
        self.folderfile = folderfile
        


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

