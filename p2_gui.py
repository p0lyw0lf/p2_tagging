from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
from io import BytesIO

from p2_tagging import Song

DEFAULT_IMAGE_DATA = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x05\xc1IDATx\x9c\xed\xdcKn\x13[\x14\x86\xd1])\xdb\t\xc6\x02\xdc\x80\x06\xd3`N\xf7\x8e\x89\xcb|\xe8\x00\xcdL\x00A?B\x08\x05\x83\xed\xdb \x8e\x8a(\x84\x97\xab\xfc\xf8\xd7\x92\xac(R\xb2u:\xe7\xab\xf2)\xcbU\x00\x00@\x90\xa6\x87\x99\xcfz\x98\tCy\xb3\xeb\x05\x0ci\xdb\x01xVU\xaf\xb7<\x13\x86\xf4oU\xfd\xb7\xebE\x0ce\xd4\xc7\xd0\xf5z\xdd\xc7X\xe8U\xd34UU\xcf\xaf~\x8d\x88\xc0\xc9\xae\x17\x00\xfb\xe4\xf5\xeb\xd7U\xdf"\xf0\xcf\x8e\x972\x08\x01\x80\x8e\xe9t\x1a\x15\x01\x01\x80\x8e\xe9t\x1a\x15\x01\x01\x80\x8eM\x00R" \x00\xd0\xd1\r@B\x04\x04\x00:n\x06\xe0\xd8# \x00\xd0\xd14MT\x04\x04\x00nH\x8a\x80\x00\xc0-R" \x00\xf0\x03\t\x11\x10\x00\xb8\xc3\xb1G@\x00\xe0\'\x8e9\x02\x02\x00\xbf\xe0X# \x00\xf0\x8b\x8e1\x02\x02\x00\xbf\xe1\xd8" \x00\xf0\x9b\x8e)\x02\x02\x00\x7f\xe0X" \x00\xf0\x87\x8e!\x02\x02\x00\x7f\xe1\xd0# \x00\xf0\x97\x0e9\x02\x02\x00[p\xa8\x11\x10\x00\xd8\x92C\x8c\x80\x00\xc0\x16\x1dZ\x04\x04\x00\xb6\xec\x90" \x00\xd0\x83C\x89\x80\x00@O\x0e!\x02\x02\x00=\xda\xf7\x08\x08\x00\xf4l\x9f# \x000\x80}\x8d\x80\x00\xc0@\xf61\x02\x02\x00\x03\xda\xb7\x08\x08\x00\x0cl\x9f" \x00\xb0\x03\xfb\x12\x01\x01\x80\x1d\xd9\x87\x08\x08\x00\xec\xd0\xae# \x00\xb0c\xbb\x8c\x80\x00\xc0\x1e\xd8U\x04\x04\x00\xf6\xc4."0\xda\xf6@8dM\xd3\xecz\twy^Uo\xae^[!\x00pe\xb5Z]\xff\\.\x97uyyY\x17\x17\x17\xf5\xee\xdd\xbb:??\xafW\xaf^\xd5\xf9\xf9y\xbd\x7f\xff\xbe...\xea\xf2\xf2\xb2\x96\xcb\xe5\xf5\xff\xad\xd7\xeb^\xd7\xd7\xc7|o\x01\xe0\x175M\xb3\xefw\x08\xbf\xcd\x1d\x00\xfc\xc4f\xe3w_\'\'\'urr\xf2\xddU\xb9\xef;\x80\xe5r\xb9\xf5\x99\x02\x00w\xd8\\\xf17\x1b\xbem\xdb\x1a\x8dF\xd5\xb6m\xb5m\xfb\xdd\xdf\x08\x00\x1c\x91\xee\xd5\xbem\xdb\x1a\x8f\xc75\x99L\xea\xf4\xf4\xb4\xce\xce\xce\xaa\xaa\x06=\x03X,\x16[\x9f)\x00p\x8b\xee\xe6\x1f\x8dF5\x99L\xea\xde\xbd{5\x9b\xcd\xea\xc1\x83\x07UUuvv6h\x00>|\xf8\xb0\xf5\x99\x02\x007ln\xe9\x9b\xa6\xa9\xb6mk2\x99\xd4\xfd\xfb\xf7k>\x9f\xd7\x93\'O\xaai\x9a\x9a\xcdf\xb5X,j\xb5Z\r\x16\x80\xb7o\xdfn}\xa6\x00\xc0-6\x9b\x7f<\x1e\xd7t:\xad\xf9|^O\x9f>\xad\xaa\xaa\xf9|^\x9f>}\xaa/_\xbe\xd4j\xb5\xba\xde\xf8}\x07\xe0\xe5\xcb\x97[\x9f)\x00p\xa5\xfb\x88os\xe87\x99Lj6\x9b\xd5\xe3\xc7\x8f\xab\xaa\xea\xe1\xc3\x87\xf5\xf1\xe3\xc7Z,\x16\xb5\\.k\xbd^\xf7\xbe\xf17^\xbcx\xb1\xf5\x99\x02\x00\xb7\xb8y\x07PU5\x1e\x8f\xeb\xd1\xa3G\xf5\xf9\xf3\xe7\xeb\xf7\xfeCm\xfe\xbe\x08\x00\xdc\xd04M\xad\xd7\xeb\xef\xce\x00\x9a\xa6\xa9\xf1x\\\xb3\xd9\xac\xbe~\xfdz\x14\x9b\xbfJ\x00\xe0V\xdd\xe7\xff\x9b\'\x02m\xdb\xd6\xe9\xe9\xe9\xd1l\xfe*\x01\x80\x1f\xea\x9e\t\xb4m{\xfd\xc9\xbf!?\xfd\xd77\x01\x80;t\x1f\t\x0eu\xda?$\x01\x80\x9f\xe8\x9e\t\x1c\x1b\x01\x80\xdftL!\x10\x00\xf8\x05\xc7\xb4\xe9\xbb|\x1f\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@\xb0Q\x1fC\x9b\xa6\xe9c,\xb0e}\xec\xd4g=\xcc\x04\xbey\xb3\xeb\x05\x00\x00\x00\x07\xeb\x7f\xc3\xf3Z\x80-\xb2\xc5>\x00\x00\x00\x00IEND\xaeB`\x82'
DEFAULT_IMAGE = Image.open(BytesIO(DEFAULT_IMAGE_DATA))

DEFAULT_FILE_EXTENSION = "m4a"
IMAGE_WIDTH=256
IMAGE_HEIGHT=256

class SongInput:
    """
    A class to handle the display and input of Song metadata.
    
    Has helper methods for reading from/writing to a corresponding
    Song class.
    
    Example usage:
    
    mainframe = ttk.Frame(root)
    s = SongInput(mainframe)
    ...
    (user loads song into Song class song_obj)
    s.load_from_song(song_obj)
    (user edits object using GUI, make callback to save song_obj)
    s.save_to_song(song_obj)
    song_obj.save_tags()
    """
    def __init__(self, container, r=0):
        image_container = ttk.Frame(container)
        image_container.grid(column=0, row=r, sticky=(N, W, S, E))
        
        self.image_data = b''
        self.image = ImageTk.PhotoImage(DEFAULT_IMAGE)
        self.image_button = ttk.Button(image_container, 
            image=self.image,
            command=self.set_image)
        self.image_button.grid(column=0, row=0)
        
        main_container = ttk.Frame(container)
        main_container.grid(column=1, row=r, sticky=(N, W, E, S))
        
        self.artists_container = ttk.Frame(main_container)
        self.album_artists_container = ttk.Frame(main_container)
        
        self.filename = StringVar()
        self.title = StringVar()
        self.album = StringVar()
        self.year = StringVar()
        
        self.artists = []
        self.artists_entries = []
        self.album_artists = []
        self.album_artists_entries = []
        
        ttk.Label(main_container, text="Filename:").grid(column=0, row=0)
        ttk.Label(main_container, textvariable=self.filename).grid(column=1, row=0, sticky=(W, E))
        ttk.Label(main_container, text="Title:").grid(column=0, row=1)
        ttk.Entry(main_container, textvariable=self.title).grid(column=1, row=1, sticky=(W, E))
        ttk.Label(main_container, text="Artists:").grid(column=0, row=2, sticky=N)
        self.artists_container.grid(column=1, row=2, sticky=(N, S, E, W))
        ttk.Label(main_container, text="Album:").grid(column=0, row=3)
        ttk.Entry(main_container, textvariable=self.album).grid(column=1, row=3, sticky=(W, E))
        ttk.Label(main_container, text="Album Artists:").grid(column=0, row=4, sticky=N)
        self.album_artists_container.grid(column=1, row=4, sticky=(N, S, E, W))
        ttk.Label(main_container, text="Year:").grid(column=0, row=5)
        ttk.Entry(main_container, textvariable=self.year).grid(column=1, row=5, sticky=(W, E))
        
        self.new_artist_entry()
        self.new_album_artist_entry()
        self.re_add_buttons()
        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(0, weight=1)
        
        image_container.columnconfigure(0, weight=1)
        image_container.rowconfigure(0, weight=1)
        
        main_container.columnconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=4)
        self.artists_container.columnconfigure(0, weight=1)
        self.album_artists_container.columnconfigure(0, weight=1)
        
        self.image_search_directory = os.getcwd()
    
    def new_artist_entry(self):
        self.add_new_entry(
            self.artists_container,
            self.artists,
            self.artists_entries
        )
        
    def new_album_artist_entry(self):
        self.add_new_entry(
            self.album_artists_container,
            self.album_artists,
            self.album_artists_entries
        )
    
    def re_add_buttons(self):
        ttk.Button(self.artists_container, text="+", command=self.new_artist_entry).pack(side="bottom", fill="x")
        ttk.Button(self.album_artists_container, text="+", command=self.new_album_artist_entry).pack(side="bottom", fill="x")
    
    def populate(self, container, variables, entries):
        for child in container.winfo_children():
            child.destroy()
        
        for var in variables:
            entries.append(self.generate_new_entry(container, variables, entries, var))
        
    def generate_new_entry(self, container, variables, entries, text_var):
        new_frame = ttk.Frame(container)
        new_frame.pack(side="top", fill="x")
        
        text_entry = ttk.Entry(new_frame, textvariable=text_var)
        text_entry.grid(column=0, row=0, sticky=(E, W))
        del_button = ttk.Button(new_frame,
            text="-", 
            width=3, 
            command=self.delete_specific_entry(
                container,
                variables,
                entries,
                text_var, new_frame
            )
        )
        del_button.grid(column=1, row=0)
        
        new_frame.columnconfigure(0, weight=1)
        
        return new_frame, text_entry
    
    def add_new_entry(self, container, variables, entries):
        text_var = StringVar()
        new_frame, text_entry = self.generate_new_entry(container, variables, entries, text_var)
        
        entries.append((new_frame, text_entry))
        variables.append(text_var)
        
    def delete_specific_entry(self, container, variables, entries, var, ent):
        def _delete_helper():
            print(ent)
            ent.pack_forget()
            ent.destroy()
            
            #entries.remove(ent)
            variables.remove(var)
            
        return _delete_helper
    
    def delete_last_entry(self, container, variables, entries):
        i = len(entries)-1
        self.delete_specific_entry(container, variables, entries, variables[i], entries[i])()
        
    def load_from_song(self, song):
        if not (song is None):
            self.filename.set(song.filename)
            self.title.set(song.title)    
            self.album.set(song.album)
            self.year.set(song.year)
            
            self.artists = []
            for artist in song.artists:
                var = StringVar()
                var.set(artist)
                self.artists.append(var)
                
            self.album_artists = []
            for album_artist in song.album_artists:
                var = StringVar()
                var.set(album_artist)
                self.album_artists.append(var)
                
            self.image_data = song.read_image()
            self.update_image(os.path.join(song.image_output_directory, song.image_filename))
        else:
            self.filename.set("No File Loaded!")
            self.title.set("")
            self.album.set("")
            self.year.set("")
            
            self.artists = [StringVar()]
            
            self.album_artists = [StringVar()]
            
            self.update_image()
            
        self.populate(self.artists_container, self.artists, self.artists_entries)
        self.populate(self.album_artists_container, self.album_artists, self.album_artists_entries)
        
        self.re_add_buttons()
        
        
    def save_to_song(self, song):
        song.title = self.title.get()
        song.album = self.album.get()
        song.year = self.year.get()
        
        song.artists = []
        for artist_var in self.artists:
            song.artists.append(artist_var.get())
            
        song.album_artists = []
        for album_artist_var in self.album_artists:
            song.album_artists.append(album_artist_var.get())
            
        song.refresh()
        
        if self.image_data:
            song.write_image(self.image_data)
        
    def set_image(self):
        filename = filedialog.askopenfilename(
            filetypes=[("PNG", "*.png"), ("All Files", "*.*")],
            title="Choose Album Art File",
            initialdir = self.image_search_directory
        )
        self.update_image(filename, update_search=True)
    
    def update_image(self, filename=None, update_search=False):
        if filename and os.path.exists(filename) and os.path.isfile(filename):
            self.image = ImageTk.PhotoImage(
                Image.open(filename)\
                .resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
            )
            with open(filename, 'rb') as f:
                self.image_data = f.read()
            if update_search:
                self.image_search_directory = os.path.dirname(filename) or os.getcwd()
        else:
            self.image = ImageTk.PhotoImage(DEFAULT_IMAGE)
            self.image_data = None
            
        self.image_button.configure(image=self.image)
        
class SongLoader:
    def __init__(self, container, indexvar, callbacks=[]):
        self.base_directory = os.getcwd()
        self.output_directory = os.path.join(self.base_directory, 'output')
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        self.current_song = None
        self.current_index = 0
        self.indexvar = indexvar
        self.file_list = []
        
        self.current_song_callbacks = []
        
    def update_current_song(self, new_song):
        self.current_song = new_song
        
        for callback in self.current_song_callbacks:
            callback(self.current_song)
    
    def set_directory(self):
        directory = filedialog.askdirectory(
            title="Choose Music Directory",
            initialdir = self.base_directory
        )
        if directory:
            self.base_directory = directory
            self.refresh_filelist()
    
    def refresh_filelist(self):
        unfiltered_list = os.listdir(self.base_directory)
        self.file_list = [filename for filename in unfiltered_list \
            if filename.endswith(DEFAULT_FILE_EXTENSION)]
        
        if len(self.file_list) > 0:
            self.load_song(self.file_list[0])
            #if 1 > self.current_index or self.current_index >= len(self.file_list) 
            #self.current_index = 1
        else:
            self.update_current_song(None)
            self.current_index = 0
            
        self.refresh_indexvar()
        
    def load_song(self, filename):
        filepath = os.path.join(self.base_directory, filename)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            song = Song(filepath, output_directory=self.output_directory)
            song.read_tags()
            self.update_current_song(song)
        else:
            self.update_current_song(None)
            
    def save_song(self):
        if not (self.current_song is None):
            self.current_song.refresh()
            self.current_song.save_tags()
        
    def set_index(self):
        # use a tk input dialog to get the next index to set
        new_index = simpledialog.askinteger(
            "Set Index",
            "Enter the new index of the song to load:",
            initialvalue = 1,
            minvalue = 1,
            maxvalue = len(self.file_list)
        )
        
        if new_index and 1 <= new_index <= len(self.file_list):
            self.load_song(self.file_list[new_index - 1])
            self.current_index = new_index
            self.refresh_indexvar()
            
    def set_output_directory(self):
        new_output_directory = filedialog.askdirectory(
            title="Choose Output Directory",
            initialdir = self.output_directory
        )
        
        if new_output_directory:
            self.output_directory = new_output_directory
        
    def dialog_load_song(self):
        # use a tk filedialog to get the next song to load
        # potentially change base directory as well?
        filename = filedialog.askopenfilename(
            filetypes=[(DEFAULT_FILE_EXTENSION.upper(), "*."+DEFAULT_FILE_EXTENSION), ("All Files", "*.*")],
            title="Choose Song",
            initialdir = os.getcwd()
        )
        
        if filename:
            self.base_directory = os.path.dirname(filename)
            song_filename = os.path.basename(filename)
            
            # Mostly copied from self.refresh_filelist(), but too many modifications
            # needed to be made
            unfiltered_list = os.listdir(self.base_directory)
            self.file_list = [filename for filename in unfiltered_list \
                if filename.endswith(DEFAULT_FILE_EXTENSION)]
                
            new_index = self.file_list.index(song_filename)
            self.current_index = new_index + 1
            self.refresh_indexvar()
            
            self.load_song(self.file_list[new_index])
        
    def increment_index(self):
        self.refresh_filelist()
        self.current_index = self.current_index + 1
        if self.current_index > len(self.file_list):
            self.current_index = 1
        
        if self.current_index != 0:
            self.load_song(self.file_list[self.current_index - 1])
            self.refresh_indexvar()
        
    def decrement_index(self):
        self.refresh_filelist()
        self.current_index = self.current_index - 1
        if self.current_index < 1:
            self.current_index = len(self.file_list)
        
        if self.current_index != 0:
            self.load_song(self.file_list[self.current_index - 1])
            self.refresh_indexvar()
        
    def refresh_indexvar(self):
        self.indexvar.set(f"{self.current_index} / {len(self.file_list)}")

def main():
    root = Tk()
    root.title("P2 Tagging")
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    bottomframe = ttk.Frame(mainframe)
    bottomframe.grid(row=1, column=0, columnspan=2, sticky=(W, E))
    bottomframe.columnconfigure(1, weight=1)
    
    songinput = SongInput(mainframe)
    indexvar = StringVar()
    songloader = SongLoader(mainframe, indexvar)
    songloader.current_song_callbacks.append(songinput.load_from_song)
    
    songloader.refresh_filelist()
    songloader.refresh_indexvar()
    
    menubar = Menu(root)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open File", command=songloader.dialog_load_song)
    filemenu.add_command(label="Open Directory", command=songloader.set_directory)
    filemenu.add_command(label="Set Index", command=songloader.set_index)
    filemenu.add_separator()
    filemenu.add_command(label="Set Output Directory", command=songloader.set_output_directory)
    filemenu.add_command(label="Load Metadata", command=lambda: print("c"))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Guess Metadata", command=lambda: print("d"))
    editmenu.add_command(label="Refresh Directory", command=songloader.refresh_filelist)
    menubar.add_cascade(label="Edit", menu=editmenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Usage", command=lambda: print("e"))
    helpmenu.add_command(label="About", command=lambda: print("f"))
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    ttk.Button(bottomframe,
        text="<",
        command=songloader.decrement_index
    ).grid(row=1, column=0, sticky=W)
    
    def full_save():
        songinput.save_to_song(songloader.current_song)
        songloader.save_song()
    ttk.Button(bottomframe,
        text="Save",
        command=full_save
    ).grid(row=1, column=1, sticky=(W,E))
    
    ttk.Button(bottomframe,
        text=">",
        command=songloader.increment_index
    ).grid(row=1, column=2, sticky=E)
    ttk.Label(bottomframe, textvariable=indexvar).grid(row=0, column=1, sticky=N)
    
    root.config(menu=menubar)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()