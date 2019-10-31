# P2 Tagging

A useful program to quickly edit metadata for a bunch of .m4a files!

Requirements:
* Python 3.8
  * mutagen
  * pillow

## Usage
1. Launch `p2_gui.py` and load the folder containing all the files whose metadata you want to edit
2. Use the *extremely* user-friendly gui to accomplish all the tasks you wish to
3. Be satisfied that you have used a piece of software written in python with little hassle

#### External command to get a bunch of m4a files from a youtube playlist
`youtube-dl -x --audio-format "m4a" --metadata-from-title "%(artist)s - %(title)s" <playlist_url>`
