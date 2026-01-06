from mutagen.mp3 import MP3 # used to read mp3 files
from mutagen.easyid3 import EasyID3 # used to read mp3 metadata
from mutagen.easymp4 import EasyMP4 # 
from mutagen import File # used to read different file types

import numpy as np 
import os # lets me interact with the operating system

import sys 
import importlib # used to import modules in runtime
import glob

import icecream
from icecream import ic as print


import tkinter as tk # for my GUI
from tkinter import filedialog # for the open file thing
from tkinter import ttk   #for my tree view display
from tkinter import messagebox #for the alerts or messages that might pop up

import sqlite3  #used for my databases

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # in order for my code to talk to spotify



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
    def __init__(self, display = None, ):
        """
        Initializes Kobraslib with display and filepath.
        Uses tkinter to make a GUI for the library menu.
        Attributes:
            display (tk.Tk): The tkinter display object.
            file (str): The path to the music file.
        """
        self.display = display
        self.musicdict = [] 
    
    def fs(self):
        """
        Docstring for fs
        
        :param self: Description
        :returns the filescanner function and the information from it
        :rtype: Any | Literal['No file selected']
        """
        return self.filescanner()
        
    def KobraGUI(self):
        """
        This will display the window, which is the basis of how this whole thing will work
        There will be a menu in which you can select add files to a viewable list. 
        
        
        Side Effects:
            Will display the main GUI which is basically the front end of all the code.
        Returns:
            It returns the display information
        
        """
        self.display = tk.Tk() #this will create the display basically
        
        self.display.geometry("1000x550") #setting up dimentions
        self.display.title("Kobras Library")
        self.display.configure(bg = "#976532") 

        label = tk.Label(self.display, text = "Welcome to Kobra's Library!!", font = ('Helvetica', 22), bg = "#967969")#creating a simple label for testing
        label.pack(padx=40, pady= 20)
        # the pack func tells python where to put the code, and the pads tell how far from the borders you want it.
        
        textbox = tk.Text(self.display, height = 3, font = ('Helvetica', 15)) #a textbox
        
        
        button = tk.Button(self.display, text = "Click for Menu!", font = ('Helvetica', 20))

       #setting up treeview in order to see the         
        
        ## Creating style 
        
        style = ttk.Style()
        style.theme_use("default")
        
        # creating colors
        
        style.configure("Treeview", background = "#D3D3D3", foreground = "black", feildbackground = "#D3D3D3")
        
        style.map('Treeview', background = [('selected', "#32778C")])
        
        #creating frame
        dbtreefame = tk.Frame(self.display)
        dbtreefame.pack(pady = 10, fill = "x")
        
        dbtfscrool = tk.Scrollbar (dbtreefame)
        dbtfscrool.pack(side = "right", fill = "both")
        
        #setting up treeview in order to see the d
        dbtree = ttk.Treeview(dbtreefame, yscrollcommand = dbtfscrool.set, selectmode = "extended") 
        
        dbtfscrool.config(command = dbtree.yview)
        
        #creating 
        columns = ("Title", "Artist", "Length", "BPM", "Date", "Genre", "Key")
        dbtree["columns"] = columns
        
        #faormatting columns
        dbtree.column("#0", width = 60, minwidth = 25)
        dbtree.column(columns[0], anchor = "center", width = 300)
        dbtree.column(columns[1], anchor ="center", width = 270)
        dbtree.column(columns[2], anchor ="center", width = 70)
        dbtree.column(columns[3], anchor ="center", width = 70)
        dbtree.column(columns[4], anchor ="center", width = 50)
        dbtree.column(columns[5], anchor ="center", width = 100)
        dbtree.column(columns[6], anchor ="center", width = 50)

        # making headings
        
        dbtree.heading("#0", text = "Index", anchor = "center")
       
        dbtree.heading(columns[0], text = "Title", anchor = "center")
        dbtree.heading(columns[1], text = "Artist", anchor = "center")
        dbtree.heading(columns[2], text = "Length", anchor = "center")
        dbtree.heading(columns[3], text = "BPM", anchor = "center")
        dbtree.heading(columns[4], text = "Date", anchor = "center")
        dbtree.heading(columns[5], text = "Genre", anchor = "center")
        dbtree.heading(columns[6], text = "Key", anchor = "center" )
        
        
        # striped rows
        
        dbtree.tag_configure('oddrow', background = "white")
        dbtree.tag_configure('evenrow', background = "#E1B57D")
        
        # Add data with a for loop
        
        connection = get_con("tutorial.db")

        query = "SELECT title, artist, length, bpm, Date FROM kobraslib"

        rows = connection.execute(query).fetchall()
        muse = 0
        
        
        for row in rows:
            if muse % 2 == 0:
                dbtree.insert(
                    parent="",
                    index="end",
                    iid=muse,
                    text=str(muse),
                    values=row,
                    tags=('evenrow',)
                )
            else:
                dbtree.insert(
                    parent="",
                    index="end",
                    iid=muse,
                    text=str(muse),
                    values=row,
                    tags=('oddrow',)
                )
            muse += 1

        

        connection.close()
                
        
        
        dbtree.pack()

       
        #this frame will have all the buttons in order to work the library 
        
        dpframe = tk.LabelFrame(self.display, bg="#967969", width = 750, padx = 20, pady = 20)
        dpframe.pack(fill = "x", expand = "yes", padx = 10)

        dpflabel = tk.Label(dpframe, text= "Functions", font = ('Helvetica', 14))
        dpflabel.grid()        
        #these are the bottons which each has a command that connects to a function with a specific purpose.
        dpfbutton1 = tk.Button(dpframe, text = "Add New Song", font = ('Helvetica', 12), width = 12, command = self.fs)
        dpfbutton2 = tk.Button(dpframe, text = "Filter by", font = ('Helvetica', 12), width = 12, command = self.viewall)
        dpfbutton3 = tk.Button(dpframe, text = "Delete Song", font = ('Helvetica', 12), width = 12)
        dpfbutton4 = tk.Button(dpframe, text = "Delete Multiple Songs", font = ('Helvetica', 12))
        dpfbutton5 = tk.Button(dpframe, text = "Exit Menu", font = ('Helvetica', 12), width = 12)
        
        
        dpfbutton1.grid(row = 0, column = 1, padx = 10, pady = 10)
        dpfbutton2.grid(row = 0, column = 2, padx = 10, pady = 10)
        dpfbutton3.grid(row = 0, column = 3, padx = 10, pady = 10)
        dpfbutton4.grid(row = 0, column = 4, padx = 10, pady = 10)
        dpfbutton5.grid(row = 0, column = 5, padx = 10, pady = 10)


        

        
        
 

        
        self.display.mainloop() #this makes the display continue consistently Im pretty sure
        
        return self.display #used so that I can use the info from it within other stuff


    def popup(self, num, message):
        """
        Docstring for popup
        
            This will be used as a pop up anytime someone has successfully added a song, 
        there's an error, or any other type of message. 
        
        These are all the types of pop ups:
        
        showinfo()
        showwarning()
        showerror()
        showquestion()
        """
        if num == 1:
            messagebox.showinfo("Hello!", message)   # ~.showinfo("title", "message")
        elif num == 2:
            messagebox.showerror("Error!!!", message)
        
    def filescanner(self):
        """
        Docstring for filescanner
        
            This function opens up the file explorer on a users computer and allows
        them to add a song to the Kobra database. 
        
        Returns:
            Will return "No file selected" if the window was closed without picking a file.
        """
        

        self.kbfile = filedialog.askopenfilename(filetypes = [("Music", "*.mp3")])
        self.kbfile
        
        if not self.kbfile:          #used if the user does not select a file
            print("No File selected.")
            return 
        
        audio = MP3(self.kbfile)
        tags = EasyID3(self.kbfile)

        print("These are the MP3 tags: \n")        
        # using ["N/A"] incase the tag does not exist, this will probably be where
        # the music brainz API will come in, but FILE SCANNER IS DONE
        title = tags.get('title', ['N/A'])[0]
        artist = tags.get('artist', ['N/A'])[0]
        min = int((audio.info.length) // 60)
        secs = int(audio.info.length % 60)
        if len(str(secs)) == 1:
            secs = f'0{str(secs)}'
        lstr = str(f'{min}:{secs}')
        
        rawbpm = tags.get('bpm')  # returns None or ['120']

        if rawbpm:
            bpm = int(float(rawbpm[0]))  # removes trailing .0
        else:
            bpm = "N/A"

        date = tags.get('date', ['N/A'])[0]
        
        musicdict = {"Title": title,    # creating a dict that will be used to iterate into the db
                     "Artist": artist,
                     "Length": lstr,
                     "BPM": bpm,
                     "Date": date}
        
        
        
        self.musicdict = musicdict
        connection = get_con("tutorial.db")
    
        
        connection = get_con("tutorial.db")
        try:
            #creation of table
            create_table(connection)
            self.insertsong(connection, musicdict["Title"], musicdict["Artist"], musicdict["Length"], musicdict["BPM"], kobra.musicdict["Date"])
            
            return musicdict
        finally:
            connection.close()  #for saftey reasons always want to close
        
    def insertsong(self, connection, title, artist, length, bpm, Date):
        """
        Docstring for insertsong
        Args:
            connection: Description
            title (str): The song title
            artist (str): The artist title
            length (str): The song length
            bpm (str): The song beats per minute
            Date (str): The song length
        Side Effects:

        """
        query = "INSERT INTO kobraslib (title, artist, length, bpm, Date) VALUES (?,?,?,?,?)"
        
        # inputing the values into the list
        try:
            with connection:
                connection.execute(query, (title, artist, length, bpm, Date))
            if "hi" =="hi":
                num = 1
                message = (f"The song: '{kobra.musicdict["Title"]}' was added!")
                self.popup(num, message)    #pop up code
        except Exception as e:
            if "hi" == "hi":     
                num = 2
                message = "You already put this song in the database. \nPlease input a different song!"
                self.popup(num, message) #pop up code
    
    def viewall(self, connection= None, condition = None ):
        """
        Args:
            Connection(str): The connection to the db
            Condition: this will be if someone picke like genre or something
            
        """
        connection = get_con("tutorial.db")
        
        query = "SELECT * FROM kobraslib"
        if condition:  #this will be where people will request the organizaion
            query += f"WHERE {condition}"
        
        try:
            with connection:
                rows = connection.execute(query).fetchall() #this will print everything within the query
            return rows
        except Exception as e:
            print(e)
        
        for song in connection:     #recursive
            print(song)
            
        connection.close()
    def create_table (self,connection):
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
            bpm TEXT,
            Date INTEGER,
            genre TEXT,
            key TEXT,
            UNIQUE(title, artist))               
        """
        
        try:
            with connection:
                connection.execute(query)     #actually runs the code
            print("Table was created!")
        except Exception as e:
            print(e)           #simply just prints the error that arises
                
      
        
            

        
        








    
    
    

    
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
    
    print(f"Title: {title}")
    print(f"Artist: {artist}")
    print(f"Length: {lstr}")
    print(f"BPM: {bpm}")
    print(f"Date: {date}")
        

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
        bpm TEXT,
        Date INTEGER,
        genre TEXT,
        key TEXT,
        UNIQUE(title, artist))               
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
    
    try:
        #creation of table
        create_table(connection)
        insertsong(connection, kobra.musicdict["Title"], kobra.musicdict["Artist"], kobra.musicdict["Length"], kobra.musicdict["BPM"], kobra.musicdict["Date"])
        cur = connection.cursor()
        
    finally:
        connection.close()  #for saftey reasons always want to close



if __name__ == "__main__":
       
    kobra = Kobraslib()
    kobra.KobraGUI()

