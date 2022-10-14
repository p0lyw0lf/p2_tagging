# P2 Tagging

A useful program to quickly edit metadata for a bunch of .m4a files!

Requirements:
* Python 3.8
  * mutagen
  * pillow
  * spotipy
  * beautifulsoup4

## Usage
1. Launch `gui.py` and load the folder containing all the files whose metadata you want to edit
2. Use the *extremely* user-friendly gui to accomplish all the tasks you wish to
3. Be satisfied that you have used a piece of software written in python with little hassle

#### External command to get a bunch of m4a files from a mixed list of Youtube/SoundCloud URLs
```
youtube-dl -x --audio-quality 0 --audio-format "m4a" --postprocessor-args "-b:a 320000" --embed-thumbnail --add-metadata -a "list.txt"
```
You need [youtube-dl](https://youtube-dl.org/) on your %PATH% for this to work. This gets everything in max 320kbps audio quality in the format this script expects, with initial metadata to start.

#### Command to convert existing, potentially metadata-ed files that aren't m4a to ones that can be edited with the script:
```
cd to/your/music/dir
./rel/path/to/p2_tagging/convert_remaining.bat
```
This converts everything to 320kbps m4a, just like what the youtube downloading one does.
