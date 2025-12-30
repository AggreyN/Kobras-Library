This is just Documentation

    So this is a 4 week plan to build my music coding project. I love music and I love coding,
so I am combining both to build this project. This is basically the layout of my plan.

WEEK 1:
    - Learn the mutagen library for music generation in Python.
    - Implementation of File System Navigation
    - Building a Basic file scanner
    * I will be pulling on the knowledge from my OOP course that I just too this fall
    to test and program this project.

WEEK 2:
    - Learn SQLite Basics 
    -  Design Database Schemes
    - Implement Data insertion
    *I do not know that much about SQL so I really need to lock in when it comes to learning
    that language. Database creation isn't that new to me but I am not comfortable with is 
    so I will definitely have to review for that

WEEK 3:
    - Install Music brainz library
    - Learning API Queries
    - Implement metada enrichment
    - Handleing multiple matches
    - Rate limiting & error Handling 
    * Honestly this will probably be my hardest week because I don't know anything 
    except error handling from the week.

WEEK 4: 
    - Create a Search inqueries
    - Build Command Line interfance
    - Add-Advanced filers
    - TESTING AND DEBUGGING
    *Also very hard week


12/22/25

    So I am trying to learn how to use the mutagen library, installing it and 
learning its classes and all that. Trying to use this website to learn about the module
Will put it in the refernces section of this doc.

12/23/25

    So what I need to do is learn the methods that will allow me to read music 
    files into a list, or at least the names/tags of them. 

12/24/24

    Merry Christmas Eve, I am currently working on trying to display the id3 tags,
(the information from the file). I do not know if I want the user to input their
directory and then pull the music from there, or ask them every time for the directory.
I don't really know how ot use pathlib/sys/os that much so I am in the process of learning how to use it for 
what is neccessary within this project. But I have to have a lot more progress before
I can move on to next weeks stuff.

    Just realized that I could make it sort of like a game where you would have a menu. So
it would have, add new song, view library, delete song. So this would all be within a class.
Would I need functions within functions?? I am pretty sure. I want the user to be able to either view all
the information, like the genre, bpm, artist, all that.

    Experienced a problem with always pushing the music example files so I used gitignore
to ignore the whole MusicExample folder. I will use a GUI, first time, to make it more interactive
this will prevent confusion and add simplicity, for the user not me unfortunately.

12/27/25

    Through watching a youtube video, I realized that there are simpler ways to create a menu.
As in there's a menu function within the tkinter module. The more you know, I will learn a lot over the next three weeks.
But I will now stop procrastinating and complete the base file scanner. But as for now the GUI 
has been 60% completed and all I need to do is add commands for functioanality.

12/28/25

    I have finished the file scanner that will be a command within the display!
It was way easier than I thought it would have to be, now I have to learn how to create,
a database in which the meta/audio data of the files will come from. As of right now,
I have typed out the directory in which the file will be opening from, but in the actual 
project, the user won't be able to pull from my directory. So I will probably change the 
path to the music folder of the user or just have them select the path that they want to be 
pulling from. But I want everything to be showing up on the GUI so idk how that will work.

12/29/29

    Now it is week 2, and its time to work on putting the data into either a csv file using SQLite
in combination with Python and implement data insertion. Then hopefully, the GUI will display the list
as a spreadsheet. Also just worked on adding a command to one of the buttons in the GUI. 

I just implemented the command for "add new song," but now i need to create another GUI based off the SQL
database that I am going to create. So for example when someone presses add new song, it will open up another
database GUI from there, while hiding the main "Starting Screen". Then from there they shuould press an "add"
song button that I will create that will then open up file scanner (will probably be named file selector),
and then you would select a song that will then automatically update the database GUI with the new song.

* maybe I will add a play song function that will act as a button when you select a song using viewlibrary().








References


Tkinter Beginner Course - Python GUI Development
    - https://www.youtube.com/watch?v=ibf5cx221hk

SQLite Tutorial Video
    - https://www.youtube.com/playlist?list=PLP9IO4UYNF0UQkBXlTMSw0CYsxv-GDkkI
    s




