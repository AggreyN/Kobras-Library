from mutagen.mp3 import MP3 # used to read mp3 files
from mutagen.easyid3 import EasyID3 # used to read mp3 metadata
from mutagen.easymp4 import EasyMP4 # 
from mutagen import File # used to read different file types


import librosa  # for audio analysis
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
from tkinter import simpledialog #for when theres a pop up where you would have to enter something


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
        self.filescanner()
        self.refresh_treeview()
        
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
        
        self.display.geometry("1200x650") #setting up dimentions
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
        self.dbtree = ttk.Treeview(dbtreefame, yscrollcommand = dbtfscrool.set, selectmode = "extended") 
        
        dbtfscrool.config(command = self.dbtree.yview)
        
        #creating 
        columns = ("Title", "Artist", "Length", "BPM", "Date", "Key", "Genre")
        self.dbtree["columns"] = columns
        
        #faormatting columns
        self.dbtree.column("#0", width = 60, minwidth = 25)
        self.dbtree.column(columns[0], anchor = "center", width = 380)
        self.dbtree.column(columns[1], anchor ="center", width = 300)
        self.dbtree.column(columns[2], anchor ="center", width = 70)
        self.dbtree.column(columns[3], anchor ="center", width = 70)
        self.dbtree.column(columns[4], anchor ="center", width = 50)
        self.dbtree.column(columns[5], anchor ="center", width = 50)
        self.dbtree.column(columns[6], anchor ="center", width = 100)

        # making headings
        
        self.dbtree.heading("#0", text = "Index", anchor = "center")
       
        self.dbtree.heading(columns[0], text = "Title", anchor = "center")
        self.dbtree.heading(columns[1], text = "Artist", anchor = "center")
        self.dbtree.heading(columns[2], text = "Length", anchor = "center")
        self.dbtree.heading(columns[3], text = "BPM", anchor = "center")
        self.dbtree.heading(columns[4], text = "Date", anchor = "center")
        self.dbtree.heading(columns[5], text = "Key", anchor = "center")
        self.dbtree.heading(columns[6], text = "Genre", anchor = "center" )
        
        
        # striped rows
        
        self.dbtree.tag_configure('oddrow', background = "white")
        self.dbtree.tag_configure('evenrow', background = "#E1B57D")
        
        # Add data with a for loop
        
        connection = get_con("tutorial.db")

        query = "SELECT title, artist, length, bpm, Date, key, genre FROM kobraslib"

        rows = connection.execute(query).fetchall()
        muse = 0
        
        
        for row in rows:
            if muse % 2 == 0:
                self.dbtree.insert(
                    parent="",
                    index="end",
                    iid=muse,
                    text=str(muse),
                    values=row,
                    tags=('evenrow',)
                )
            else:
                self.dbtree.insert(
                    parent="",
                    index="end",
                    iid=muse,
                    text=str(muse),
                    values=row,
                    tags=('oddrow',)
                )
            muse += 1

        

        connection.close()
                
        
        
        self.dbtree.pack()

       
        #this frame will have all the buttons in order to work the library 
        
        dpframe = tk.LabelFrame(self.display, bg="#967969", width = 750, padx = 20, pady = 20)
        dpframe.pack(fill = "x", expand = "yes", padx = 10)

        dpflabel = tk.Label(dpframe, text= "Functions", font = ('Helvetica', 14))
        dpflabel.grid()        
        #these are the bottons which each has a command that connects to a function with a specific purpose.
        dpfbutton1 = tk.Button(dpframe, text = "Add New Song", font = ('Helvetica', 12), width = 13, command = self.fs)
        dpfbutton2 = tk.Button(dpframe, text = "Filter by", font = ('Helvetica', 12), width = 12, command = self.filterby)
        dpfbutton3 = tk.Button(dpframe, text = "Delete Song", font = ('Helvetica', 12), width = 12, command = self.delmusic)
        dpfbutton4 = tk.Button(dpframe, text = "Delete All Songs", font = ('Helvetica', 12), width = 12, command =self.delete_all)
        dpfbutton5 = tk.Button(dpframe, text = "Exit Menu", font = ('Helvetica', 12), width = 12, command = self.exitmenu)
        dpfbutton6 = tk.Button(dpframe, text = "Refresh", font=('Helvetica', 12), width=12, command=self.refresh_treeview)
        
        dpfbutton7 = tk.Button(dpframe, text = "Filter by Artist", font=('Helvetica', 12), width = 12, command = lambda: self.fpopup("artist"))
        dpfbutton8 = tk.Button(dpframe, text = "Filter by BPM", font=('Helvetica', 12), width = 12, command = lambda: self.fpopup("bpm"))
        dpfbutton9 = tk.Button(dpframe, text = "Filter by Date", font=('Helvetica', 12), width = 12, command = lambda: self.fpopup("Date"))
        dpfbutton10 = tk.Button(dpframe, text = "Filter by Genre", font=('Helvetica', 12), width = 12, command = lambda: self.fpopup("genre"))
        dpfbutton11 = tk.Button(dpframe, text = "Filter by Key", font=('Helvetica', 12), width = 12, command = lambda: self.fpopup("key"))

        # When I ran the cade originally, all the popups came at the same time so
        # what I did was use lambda so that I could still have the column name
        # that were parameters
        
        
        
        dpfbutton1.grid(row = 1, column = 0, padx = 10, pady = 10)
        dpfbutton2.grid(row = 0, column = 0, padx = 10, pady = 10)
        dpfbutton3.grid(row = 1, column = 1, padx = 10, pady = 10)
        dpfbutton4.grid(row = 1, column = 2, padx = 10, pady = 10)
        dpfbutton5.grid(row = 1, column = 3, padx = 10, pady = 10)
        dpfbutton6.grid(row = 1, column = 4, padx = 10, pady = 10)
        dpfbutton7.grid(row = 0, column = 1, padx = 10, pady = 10)
        dpfbutton8.grid(row = 0, column = 2, padx = 10, pady = 10)
        dpfbutton9.grid(row = 0, column = 3, padx = 10, pady = 10)
        dpfbutton10.grid(row = 0, column = 4, padx = 10, pady = 10)
        dpfbutton11.grid(row = 0, column = 5, padx = 10, pady = 10)

     
        
 

        
        self.display.mainloop() #this makes the display continue consistently Im pretty sure
        
        return self.display #used so that I can use the info from it within other stuff

    def refresh_treeview(self):
        """
        This will be used as a button for refreshing data so that you won't have to
        close and reopen the app for it to work
        """
        # Clear current rows
        for row in self.dbtree.get_children():
            self.dbtree.delete(row)

        # Re-query the DB
        connection = get_con("tutorial.db")
        query = "SELECT id, title, artist, length, bpm, Date, key, genre FROM kobraslib"

        rows = connection.execute(query).fetchall()
        

        # Re-insert with alternating tags
        muse = 0
        for row in rows:
            dbid = row[0]
            songdata = row[1:] #everything but the id
            
            tag = 'evenrow' if muse % 2 == 0 else 'oddrow'
            
            self.dbtree.insert(
                parent = "",
                index = "end",
                iid = dbid,
                text = str(muse),
                values = songdata,
                tags = (tag,)
            )
            muse += 1
        
        connection.close()
    
    def exitmenu(self):
        """
        Docstring for exitmenu
        
        This will just close the menu when pressed.
        """
        self.display.destroy()  
    
    def delmusic(self):
        """
        A function that will be used as a delete button command
        - Allow user to delete what they cliack, or delete by the ID of the song.
        - Will automatically use self.refresh to update after deletion, maybe ask a pop up
        
        - ask pop up, are you sure you wanna delete
        
        
        """
        # Get the selected item from treeview
        selected = self.dbtree.selection()
        
        # Checking if something is selected
        if not selected:
            self.popup(2, "Please select a song to delete!")
    
        item = self.dbtree.item(selected[0])
        values = item['values']  # This gets [title, artist, length, bpm, date, key, genre]
        title = values[0]
        artist = values[1]
        
        confirm = messagebox.askyesno("Confirm Delete",        # asks question for confirmation
                              "Are you sure you want to delete this song?")
        
        if confirm:
            connection = get_con("tutorial.db")
            query = "DELETE FROM kobraslib WHERE id = ?"    #giving parameter so that there isn't direct SQL implementation
            try:
                with connection:
                    connection.execute(query, ((selected[0]),))  #the comma is for the code to to know that it is a tutple
                    message = f"{title} by {artist} was deleted :("  #instead of just printing the id of the song, the title and artist get printed
                    num = 1
                    self.popup(num, message)
            except Exception as e:
                message = str(e)
                num = 2 
                self.popup(num, message)
            self.refresh_treeview()
        elif not confirm:
            self.popup(2, f"{title} by {artist} was deleted :)")
            return
    
        
            
        print(self.dbtree.item(selected[0])) # prints all data from the song
           
            
    def fpopup(self, column):
        """
        Asks whether the filter is genral or specific and then applies it
        
        Args:
            column(str): The Column that will be filtered
        Returns:
            and updated treevie
        """     
        
        choice = messagebox.askquestion(
        "Filter Type",
        f"Do you want a GENERAL filter or a SPECIFIC filter for {column}?\n\n"
        "Yes = Specific\nNo = General"
    )

        connection = get_con("tutorial.db")

        try:
            if choice == "yes":
                # Specific value filter
                value = simpledialog.askstring(
                    "Specific Filter",
                    f"Enter value for {column} (e.g. E#, 128, Hip-Hop):"
                )

                if not value:
                    return

                query = f"""
                    SELECT id, title, artist, length, bpm, Date, key, genre
                    FROM kobraslib
                    WHERE {column} = ?
                """
                rows = connection.execute(query, (value,)).fetchall()
                self.update_trvrows(rows)
            elif column == "key" and choice != "yes":
                #Creating an order for the key values 
                query = """
                    SELECT id, title, artist, length, bpm, Date, key, genre
                    FROM kobraslib
                    ORDER BY CASE key
                        WHEN 'C' THEN 1
                        WHEN 'C#' THEN 2
                        WHEN 'D' THEN 3
                        WHEN 'D#' THEN 4
                        WHEN 'E' THEN 5
                        WHEN 'F' THEN 6
                        WHEN 'F#' THEN 7
                        WHEN 'G' THEN 8
                        WHEN 'G#' THEN 9
                        WHEN 'A' THEN 10
                        WHEN 'A#' THEN 11
                        WHEN 'B' THEN 12
                    END ASC
                """
                rows = connection.execute(query).fetchall()
                self.update_trvrows(rows)
                return

            else:
                query = f"""
                    SELECT id, title, artist, length, bpm, Date, key, genre
                    FROM kobraslib
                    ORDER BY {column} ASC
                """
                rows = connection.execute(query).fetchall()
                self.update_trvrows(rows)
        
        except Exception as e:
            self.popup(2, str(e))
        finally:
            connection.close()
    def update_trvrows(self, rows):
        """
        Clears and repopulates treeview using provided DB rows.
        
        Args
        """

        for item in self.dbtree.get_children(): #delets everything within the 
            self.dbtree.delete(item)

        for index, row in enumerate(rows):
            tag = "evenrow" if index % 2 == 0 else "oddrow" #anoter conditional expression my professor would be proud
            self.dbtree.insert(
                parent="",
                index="end",
                iid=row[0],
                text=str(index),
                values=row[1:],
                tags=(tag,)
            )
    
    def popup(self, num, message = None):
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
        elif num == 3 and message == None:
            self.filterArt = simpledialog.askstring("You will filter by:", "Filter by:")
        
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
            num = 1
            message = "No File Selected"
            self.popup(num, message)
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
        
        
        
        key = self.detect_key(self.kbfile)
        
        # 1. Try embedded tag
        raw_genre = tags.get('genre')
        genre = raw_genre[0].strip() if raw_genre and raw_genre[0].strip() else None

        if not genre:
            genre = self.fetchgenre(artist, title)

        if not genre:
            genre = simpledialog.askstring(
                "Genre Required",
                "Genre could not be determined.\nPlease enter one:"
            )
            if not genre:
                return

        genre = genre.strip().title()
                

        if rawbpm:
            bpm = int(float(rawbpm[0]))  # removes trailing .0
        else:
            bpm = "N/A"

        date = tags.get('date', ['N/A'])[0]
        
        musicdict = {"Title": title,    # creating a dict that will be used to iterate into the db
                     "Artist": artist,
                     "Length": lstr,
                     "BPM": bpm,
                     "Date": date,
                     "Key": key,
                     "Genre": genre}
        
        
        
        self.musicdict = musicdict
        connection = get_con("tutorial.db")
    
        
        connection = get_con("tutorial.db")
        try:
            #creation of table
            create_table(connection)
            self.insertsong(connection, musicdict["Title"], musicdict["Artist"], musicdict["Length"], 
                            musicdict["BPM"], kobra.musicdict["Date"], kobra.musicdict["Key"], musicdict["Genre"])
            
            return musicdict
        finally:
            connection.close()  #for saftey reasons always want to close
    def delete_all(self):
        """
        Delete all songs from database with double confirmation
        """
        confirm = messagebox.askyesno(
            "DANGER!", 
            "Are you ABSOLUTELY SURE you want to delete ALL songs?\n\nThis cannot be undone!"
        )
        
        if confirm:
            # Double confirm
            double_confirm = messagebox.askyesno(
                "Final Warning",
                "This will permanently delete your entire library. Continue?"
            )
            
            if double_confirm:
                connection = get_con("tutorial.db")
                try:
                    with connection:
                        connection.execute("DELETE FROM kobraslib")
                    self.popup(1, "All songs deleted!")
                    self.refresh_treeview() #automatically refreshing screen
                except Exception as e:
                    self.popup(2, f"Error: {str(e)}")
                finally:
                    connection.close()


    def fetchgenre(self, artist, title):
        """
        Fetches genre from MusicBrainz API based on artist and title.
        
        Args:
            artist (str): The artist name
            title (str): The song title
        
        Returns:
            str or None: The genre if found, otherwise None
        """
        import requests
        import time
        
        try:
            # MusicBrainz requires a User-Agent header
            headers = {
                'User-Agent': 'KobrasLibrary/1.0 (ayertey.narh.24@gmail.com)'
            }
            
            # Search for the recording
            search_url = "https://musicbrainz.org/ws/2/recording/"
            params = {
                'query': f'recording:"{title}" AND artist:"{artist}"',
                'fmt': 'json',
                'limit': 1
            }
            
            response = requests.get(search_url, params=params, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('recordings'):
                    recording_id = data['recordings'][0]['id']
                    
                    # Get tags for this recording
                    time.sleep(1)  # Rate limiting - be nice to MusicBrainz
                    tags_url = f"https://musicbrainz.org/ws/2/recording/{recording_id}"
                    tag_params = {'inc': 'tags', 'fmt': 'json'}
                    
                    tag_response = requests.get(tags_url, params=tag_params, headers=headers)
                    
                    if tag_response.status_code == 200:
                        tag_data = tag_response.json()
                        tags = tag_data.get('tags', [])
                        
                        if tags:
                            # Return the most popular tag (highest count)
                            top_tag = max(tags, key=lambda x: x.get('count', 0))
                            return top_tag['name'].title()
            
            return None
            
        except Exception as e:
            print(f"MusicBrainz fetch error: {e}")
        return None

    def detect_key(self, file):
            """
            Docstring for detect_key
            
            Used in the filescanner function for detecing the key of the file.
            
            Args:
                file(str): This is the file line that contains the music
            Returns:
                detected(str): The string of the key of the file
            """
            y, sr = librosa.load(file, sr=None)
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)  # chroma features
            avg_chroma = np.mean(chroma, axis=1)
            keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            detected = keys[np.argmax(avg_chroma)]
            return detected
        
    def insertsong(self, connection, title, artist, length, bpm, Date, Key, genre):
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
        query = "INSERT INTO kobraslib (title, artist, length, bpm, Date, key, genre) VALUES (?,?,?,?,?,?,?)"
        
        # inputing the values into the list
        try:
            with connection:
                connection.execute(query, (title, artist, length, bpm, Date, Key, genre))
            if "hi" =="hi":
                num = 1
                message = (f"The song: '{kobra.musicdict["Title"]}' was added!")
                self.popup(num, message)    #pop up code

        except Exception as e:
            if "hi" == "hi":     
                num = 2
                message = "You already put this song in the database. \nPlease input a different song!"
                self.popup(num, message) #pop up code
    
    def filterby(self, condition = None ):
        """
        Args:
            Connection(str): The connection to the db
            Condition: this will be if someone picke like genre or something
            
        """
        connection = get_con("tutorial.db")
        
        artist = self.popup(3)
        artist
        
        query = f"SELECT * FROM kobraslib WHERE artist = {artist}"
        if condition:  #this will be where people will request the organizaion
            query += f"WHERE {condition}"
        
        try:
            with connection:
                rows = connection.execute(query).fetchall() #this will print everything within the query
            return rows
        except Exception as e:
            self.popup(2, str(e))
        
            
        connection.close()
    def create_table (self,connection):
        """
        Args:
            Connection (str): The connection to the database
        Side Effects:
            Creates the table that I need 
        Query - A query is a request for data stored in a data 
        The unique title/artist makes sure that there is no duplciates within it
        """
        query = """
        CREATE TABLE IF NOT EXISTS kobraslib (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT,
            length INTEGER,
            bpm INTEGER,
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
    print(mp3_file) #this is to have the files print out nice 




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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        artist TEXT,
        length INTEGER,
        bpm INTEGER,
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
        cur = connection.cursor()
        
    finally:
        connection.close()  #for saftey reasons always want to close
main()


if __name__ == "__main__":
       
    kobra = Kobraslib()
    kobra.KobraGUI()

