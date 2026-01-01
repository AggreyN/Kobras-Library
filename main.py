from mutagen.mp3 import MP3 # used to read mp3 files
from mutagen.easyid3 import EasyID3 # used to read mp3 metadata
from mutagen.easymp4 import EasyMP4 # 
from mutagen import File # used to read different file types

import numpy as np 
import os # lets me interact with the operating system

import sys 
import importlib # used to import modules in runtime
import glob
import pprint

import tkinter as tk # for my GUI
from tkinter import filedialog # for the open file thing

import sqlite3  #used for my databases


class Kobraslib():
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
    def __init__(self, display = None, file = None ):
        """
        Initializes Kobraslib with display and filepath.
        Uses tkinter to make a GUI for the library menu.
        Attributes:
            display (tk.Tk): The tkinter display object.
            file (str): The path to the music file.
        """
        self.display = display
        self.file = file
        self.musicdict = {} 
    
    def fs():
        return Kobraslib.filescanner()
    def KobraGUI(display):
        """
        This will display the window, which is the basis of how this whole thing will work
        There will be a menu in which you can select add files to a viewable list. 
        
        Side Effects:
            Will display the main GUI which is basically the front end of all the code.
        """
        display = tk.Tk() #this will create the display basically
        
        display.geometry("500x550") #setting up dimentions
        display.title("Kobras Library")
        display.configure(bg = "#976532") 

        label = tk.Label(display, text = "Welcome to Kobra's Library!!", font = ('Helvetica', 22), bg = "#967969")#creating a simple label for testing
        label.pack(padx=40, pady= 20)
        # the pack func tells python where to put the code, and the pads tell how far from the borders you want it.
        
        textbox = tk.Text(display, height = 3, font = ('Helvetica', 15)) #a textbox
        
        
        button = tk.Button(display, text = "Click for Menu!", font = ('Helvetica', 20))
        
        #this frame will have all the buttons in order to work the library 
        
        dpframe = tk.Frame(display, bg="#967969", height = 100, padx = 20, pady = 40)
        dpframe.pack(side = "top", fill = "y")

        dpflabel = tk.Label(dpframe, text= "Menu", font = ('Helvetica', 30)).pack(pady = 10, side = "top")
        
        dpfbutton1 = tk.Button(dpframe, text = "Add New Song", font = ('Helvetica', 18), width = 20, command = Kobraslib.fs)
        dpfbutton2 = tk.Button(dpframe, text = "View Library", font = ('Helvetica', 18), width = 20)
        dpfbutton3 = tk.Button(dpframe, text = "Delete Song", font = ('Helvetica', 18), width = 20)
        dpfbutton4 = tk.Button(dpframe, text = "Exit Menu", font = ('Helvetica', 18), width = 20)

        dpfbutton1.pack(pady = 5)
        dpfbutton2.pack(pady = 5)
        dpfbutton3.pack(pady = 5)
        dpfbutton4.pack(pady = 5)
        
        menubar = tk.Menu(display)

        display.config(menu=menubar)

        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)



        
        display.mainloop() #this makes the display continue consistently Im pretty sure
        
        return display #used so that I can use the info from it within other stuff
    def filescanner():
        """
        Docstring for filescanner
        
            This function opens up the file explorer on a users computer and allows
        them to add a song to the Kobra database. 
        
        Returns:
            Will return "No file selected" if the window was closed without picking a file.
        """

        kbfile = filedialog.askopenfilename(filetypes = [("Music", "*.mp3")])
        kbfile
        
        if not kbfile:          #used if the user does not select a file
            print("No File selected.")
            return 
        
        audio = MP3(kbfile)
        tags = EasyID3(kbfile)

        print("These are the MP3 tags: \n")        
        # using ["N/A"] incase the tag does not exist, this will probably be where
        # the music brainz API will come in, but FILE SCANNER IS DONE
        title = tags.get('title', ['N/A'])[0]
        artist = tags.get('artist', ['N/A'])[0]
        min = int((audio.info.length) // 60)
        secs = int(audio.info.length % 60)
        lstr = str(f'{min}:{secs}')
        
        rawbpm = tags.get('bpm')  # returns None or ['120']

        if rawbpm:
            bpm = int(float(rawbpm[0]))  # removes trailing .0
        else:
            bpm = "N/A"

        date = tags.get('date', ['N/A'])[0]
        
        print(f"Title: {title}")
        print(f"Artist: {artist}")
        print(f"Length: {lstr}")
        print(f"BPM: {bpm}")
        print(f"Date: {date}")
        
        musicdict = {"Title": title,
                     "Artist": artist,
                     "Length": lstr,
                     "BPM": bpm,
                     "Date": date}
        print(musicdict)
        
        return kbfile
       


       
kobra = Kobraslib()
kobra.KobraGUI()
    
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
    
        

    prefix = "C:\\Users\\aggre\\OneDrive\\Documents\\Coding Projects\\Kobras-Library\\MusicExamples\\" #for simplicity purposes


    #pulling from a file and displaying the tags

    mp3_file = EasyID3(prefix + 'Molotov.mp3')
    print("MP3 Tags:")
    pprint.pprint(mp3_file) #this is to have the files print out nice 



    # Access specific tags:
    print(f"Title: {mp3_file['title']}")
    print(f"Artist: {mp3_file['artist']}")

# after watching a youtube video, I think that it is easier to run things 
# through functions for sql.

def get_con(dbname):
    """
    Docstring for get_con
    
    This will act as a basis for establishing a connection to the database.
    
    Args:
        dbname (str): This is the name of the database that will be created, it will
        probably be "kblib". 
    Returns:
         sqlite3.connect(dbname) (str) - Returning the info from the connection
    Raises:
        Whatever error that comes from when something wrong is put into the parameter
        ofr get_con()
    """
    try:
        return sqlite3.connect(dbname) # practice for data bases, this connects to the db and creates on if not made
    except Exception as e:
        print(f"Error: {e}") # if a number ot something is put in here, this just raises an exception for it
        raise

def create_table (connection):
    """
    Args:
        Connection (str): The connection to the database
    Side Effects:
        Creates the table that I need 
    Query - A query is a request for data stored in a data 
    """
    query = """
    CREATE TABLE IF NOT EXISTS kobraslib (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        artist TEXT,
        length INTEGER,
        bPM INTEGER,
        genre TEXT,
        key TEXT)               
    """
    try:
        with connection:
            connection.execute(query)     #actually runs the code
        print("Table was created!")
    except Exception as e:
        print(e)           #simply just prints the error that arises
            


def main():
    """
    Docstring for main
    
    Used to run the code for kblib database
    """
    connection = get_con("tutorial.db")
    create_table(connection)



if __name__ == "__main__":
    pass
    
