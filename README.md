Kobras Music Library 🎵

A Python desktop application for organizing and managing your music collection with automatic metadata detection and intelligent audio analysis.

Features
    🎵 Automatic Metadata Extraction - Reads title, artist, album, genre, date, and BPM from MP3 files
    🎹 Musical Key Detection - Uses Librosa to automatically detect the musical key of songs
    🥁 Intelligent BPM Detection - Automatically detects tempo from audio when tags are missing
    🌐 MusicBrainz API Integration - Automatically fetches missing genre information
    🔍 Advanced Filtering - Filter by artist, genre, BPM, date, or musical key
    📊 SQLite Database - Efficient local storage with automatic duplicate prevention
    🎨 Clean GUI - Professional treeview interface with sortable columns
    ⚡ Auto-Refresh - Real-time updates after adding or deleting songs

Screenshots
Main Interface
The main window displays your entire music library with sortable columns:

Index, Title, Artist, Length, BPM, Date, Key, Genre

Filtering Options

Specific Filter: Find exact matches (e.g., "Hip-Hop", "C#", "128 BPM")
General Filter: Sort entire library by any column
Musical Key Ordering: Special chromatic ordering (C → C# → D → ... → B)

Installation
Prerequisites

Python 3.7 or higher
Windows, macOS, or Linux

Step 1: Clone the Repository
bashgit clone https://github.com/AggreyN/Kobras-Library.git
cd Kobras-Library
Step 2: Install Dependencies
bashpip install mutagen librosa numpy tkinter requests
Or using requirements.txt:
bashpip install -r requirements.txt
Step 3: Run the Application
bashpython main.py
```

## Usage

### Adding Songs

1. Click **"Add New Song"** button
2. Select an MP3 file from your computer
3. Metadata is automatically extracted:
   - If BPM is missing → Automatically detected from audio
   - If Genre is missing → Fetched from MusicBrainz API
   - If API fails → Prompted to enter manually
4. Song appears in your library instantly

### Filtering Your Library

#### Specific Filtering
1. Click any **"Filter by [Category]"** button
2. Select **"Yes"** for specific filter
3. Enter the exact value you're looking for
4. Results show only matching songs

**Example**: Filter by Genre → Specific → "R&B"

#### General Filtering (Sorting)
1. Click any **"Filter by [Category]"** button
2. Select **"No"** for general filter
3. Library is sorted by that column

**Example**: Filter by Date → General → Shows all songs sorted by year

#### Musical Key Filtering
- **Specific**: Find all songs in a particular key (e.g., "C#")
- **General**: Sort by chromatic order (C → C# → D → D# → E → F → F# → G → G# → A → A# → B)

### Deleting Songs

#### Delete Single Song
1. Select a song in the treeview
2. Click **"Delete Song"**
3. Confirm deletion
4. Song is removed from database and display

#### Delete All Songs
1. Click **"Delete All Songs"**
2. Confirm twice (irreversible!)
3. Entire library is cleared

### Other Functions

- **Refresh**: Manually reload the treeview from database
- **Exit Menu**: Close the application
- **Fullscreen**: Treeview automatically expands to fill window

## Database Schema

**Table: kobraslib**

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-incrementing primary key |
| title | TEXT | Song title (required) |
| artist | TEXT | Artist name |
| length | TEXT | Song duration (MM:SS format) |
| bpm | TEXT | Beats per minute |
| Date | TEXT | Release year |
| genre | TEXT | Music genre |
| key | TEXT | Musical key (C, C#, D, etc.) |

**Constraints:**
- `UNIQUE(title, artist)` - Prevents duplicate songs

## How It Works

### Metadata Extraction Pipeline

1. **File Tag Reading** (Mutagen)
   - Extracts existing ID3 tags from MP3 files
   - Fast and reliable for properly tagged files

2. **Audio Analysis** (Librosa)
   - **BPM Detection**: Analyzes first 30 seconds of audio to detect tempo
   - **Key Detection**: Uses chromagram analysis to identify musical key

3. **API Enrichment** (MusicBrainz)
   - Searches for missing genre information
   - Rate-limited to 1 request per second
   - Falls back to user input if unavailable

4. **Database Storage** (SQLite)
   - Stores all metadata locally
   - Prevents duplicates automatically
   - Enables fast filtering and searching

## Technical Details

### Key Technologies
- **mutagen** - MP3 metadata extraction
- **librosa** - Audio signal processing (BPM, key detection)
- **tkinter** - GUI framework
- **sqlite3** - Local database
- **requests** - MusicBrainz API calls
- **numpy** - Numerical computations

### Performance Notes
- **BPM Detection**: Takes 5-10 seconds per song (analyzes audio)
- **Key Detection**: Takes 10-15 seconds per song (full file analysis)
- **Genre Fetching**: Takes 2-3 seconds per song (API request + rate limit)
- **Tag Reading**: Instant (reads file header only)

### File Support
Currently supports:
- ✅ MP3 (.mp3)

Future support planned:
- WAV (.wav)
- M4A (.m4a)
- FLAC (.flac)

## Project Structure
```
Kobras-Library/
├── main.py              # Main application file
├── tutorial.db          # SQLite database (auto-generated)
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── MusicExamples/       # Test music folder (optional)



Troubleshooting


"No BPM tag found, detecting from audio..."

   This is normal for files without BPM tags
   Detection takes 5-10 seconds
   If detection fails, you'll be prompted to enter manually

"MusicBrainz fetch error"

   Check your internet connection
   MusicBrainz API may be temporarily down
   You'll be prompted to enter genre manually

Song not appearing after adding

   Click "Refresh" button
   Check console for error messages
   Ensure song doesn't already exist (title + artist must be unique)

Database corrupted

   Close the application
   Delete tutorial.db file
   Restart the application (creates fresh database)

Known Limitations

   Only supports MP3 files currently
   BPM detection accuracy: ~70-85% (depends on song style)
   Key detection may struggle with:
      Atonal or experimental music
      Songs with key changes
      Classical music


MusicBrainz genre tags may be inconsistent or missing

Future Enhancements

 Support for WAV, FLAC, M4A files
 Playlist creation and management
 Export library to CSV/JSON
 Album artwork display
 Multiple file upload at once
 Search bar for quick filtering
 Statistics dashboard (most played genre, average BPM, etc.)
 Spotify API integration for additional metadata
 Dark mode theme

Development Timeline
This project was completed as part of a 4-week coding challenge:

Week 1: File handling and metadata extraction ✅
Week 2: Database setup and GUI development ✅
Week 3: MusicBrainz API integration ✅
Week 4: Filtering system and polish ✅

Bonus Features Added:

Librosa key detection (beyond original scope)
Automatic BPM detection from audio
Advanced filtering with chromatic key ordering



License
This project is open source and available under the MIT License.
   
Credits
   Developer: Aggrey Narh

APIs & Libraries:
   MusicBrainz - Open music encyclopedia
   Librosa - Python audio analysis
   Mutagen - Audio metadata handling

Contact

GitHub: @AggreyN
Email: ayertey.narh.24@gmail.com
Project Link: https://github.com/AggreyN/Kobras-Library

Acknowledgments

Youtube/Python Website/Ai for project guidance
MusicBrainz community for maintaining the open music database
Stack Overflow community for troubleshooting help


Made with ❤️, Python, and SQL