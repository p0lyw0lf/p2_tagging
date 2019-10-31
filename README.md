# P2 Tagging

A useful program to quickly edit metadata for a bunch of .m4a files!

Requirements:
* Python 3.6+
* * mutagen
* * pillow
* ~~ffmpeg~~ maybe not anymore? idk

## Usage
1. Launch `p2_gui.py` and load the folder containing all the files whose metadata you want to edit
2. Use the extremely user-friendly gui to accomplish all the tasks you wish to
3. Be satisfied that you have used a piece of software written in python with little hassle

youtube-dl -x --audio-format "m4a" --metadata-from-title "%(artist)s - %(title)s" --playlist-start 78