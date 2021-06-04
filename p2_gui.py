import io
import os
from tkinter import *
from tkinter import ttk, filedialog, simpledialog

from mutagen.mp4 import AtomDataType
from PIL import Image, ImageTk

from p2_tagging import Song
from p2_scrape import ScrapeHandler, load_image_from_url
from p2_spotifyscrape import SpotifyScraper


DEFAULT_IMAGE_DATA = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x05\xc1IDATx\x9c\xed\xdcKn\x13[\x14\x86\xd1])\xdb\t\xc6\x02\xdc\x80\x06\xd3`N\xf7\x8e\x89\xcb|\xe8\x00\xcdL\x00A?B\x08\x05\x83\xed\xdb \x8e\x8a(\x84\x97\xab\xfc\xf8\xd7\x92\xac(R\xb2u:\xe7\xab\xf2)\xcbU\x00\x00@\x90\xa6\x87\x99\xcfz\x98\tCy\xb3\xeb\x05\x0ci\xdb\x01xVU\xaf\xb7<\x13\x86\xf4oU\xfd\xb7\xebE\x0ce\xd4\xc7\xd0\xf5z\xdd\xc7X\xe8U\xd34UU\xcf\xaf~\x8d\x88\xc0\xc9\xae\x17\x00\xfb\xe4\xf5\xeb\xd7U\xdf"\xf0\xcf\x8e\x972\x08\x01\x80\x8e\xe9t\x1a\x15\x01\x01\x80\x8e\xe9t\x1a\x15\x01\x01\x80\x8eM\x00R" \x00\xd0\xd1\r@B\x04\x04\x00:n\x06\xe0\xd8# \x00\xd0\xd14MT\x04\x04\x00nH\x8a\x80\x00\xc0-R" \x00\xf0\x03\t\x11\x10\x00\xb8\xc3\xb1G@\x00\xe0\'\x8e9\x02\x02\x00\xbf\xe0X# \x00\xf0\x8b\x8e1\x02\x02\x00\xbf\xe1\xd8" \x00\xf0\x9b\x8e)\x02\x02\x00\x7f\xe0X" \x00\xf0\x87\x8e!\x02\x02\x00\x7f\xe1\xd0# \x00\xf0\x97\x0e9\x02\x02\x00[p\xa8\x11\x10\x00\xd8\x92C\x8c\x80\x00\xc0\x16\x1dZ\x04\x04\x00\xb6\xec\x90" \x00\xd0\x83C\x89\x80\x00@O\x0e!\x02\x02\x00=\xda\xf7\x08\x08\x00\xf4l\x9f# \x000\x80}\x8d\x80\x00\xc0@\xf61\x02\x02\x00\x03\xda\xb7\x08\x08\x00\x0cl\x9f" \x00\xb0\x03\xfb\x12\x01\x01\x80\x1d\xd9\x87\x08\x08\x00\xec\xd0\xae# \x00\xb0c\xbb\x8c\x80\x00\xc0\x1e\xd8U\x04\x04\x00\xf6\xc4."0\xda\xf6@8dM\xd3\xecz\twy^Uo\xae^[!\x00pe\xb5Z]\xff\\.\x97uyyY\x17\x17\x17\xf5\xee\xdd\xbb:??\xafW\xaf^\xd5\xf9\xf9y\xbd\x7f\xff\xbe...\xea\xf2\xf2\xb2\x96\xcb\xe5\xf5\xff\xad\xd7\xeb^\xd7\xd7\xc7|o\x01\xe0\x175M\xb3\xefw\x08\xbf\xcd\x1d\x00\xfc\xc4f\xe3w_\'\'\'urr\xf2\xddU\xb9\xef;\x80\xe5r\xb9\xf5\x99\x02\x00w\xd8\\\xf17\x1b\xbem\xdb\x1a\x8dF\xd5\xb6m\xb5m\xfb\xdd\xdf\x08\x00\x1c\x91\xee\xd5\xbem\xdb\x1a\x8f\xc75\x99L\xea\xf4\xf4\xb4\xce\xce\xce\xaa\xaa\x06=\x03X,\x16[\x9f)\x00p\x8b\xee\xe6\x1f\x8dF5\x99L\xea\xde\xbd{5\x9b\xcd\xea\xc1\x83\x07UUuvv6h\x00>|\xf8\xb0\xf5\x99\x02\x007ln\xe9\x9b\xa6\xa9\xb6mk2\x99\xd4\xfd\xfb\xf7k>\x9f\xd7\x93\'O\xaai\x9a\x9a\xcdf\xb5X,j\xb5Z\r\x16\x80\xb7o\xdfn}\xa6\x00\xc0-6\x9b\x7f<\x1e\xd7t:\xad\xf9|^O\x9f>\xad\xaa\xaa\xf9|^\x9f>}\xaa/_\xbe\xd4j\xb5\xba\xde\xf8}\x07\xe0\xe5\xcb\x97[\x9f)\x00p\xa5\xfb\x88os\xe87\x99Lj6\x9b\xd5\xe3\xc7\x8f\xab\xaa\xea\xe1\xc3\x87\xf5\xf1\xe3\xc7Z,\x16\xb5\\.k\xbd^\xf7\xbe\xf17^\xbcx\xb1\xf5\x99\x02\x00\xb7\xb8y\x07PU5\x1e\x8f\xeb\xd1\xa3G\xf5\xf9\xf3\xe7\xeb\xf7\xfeCm\xfe\xbe\x08\x00\xdc\xd04M\xad\xd7\xeb\xef\xce\x00\x9a\xa6\xa9\xf1x\\\xb3\xd9\xac\xbe~\xfdz\x14\x9b\xbfJ\x00\xe0V\xdd\xe7\xff\x9b\'\x02m\xdb\xd6\xe9\xe9\xe9\xd1l\xfe*\x01\x80\x1f\xea\x9e\t\xb4m{\xfd\xc9\xbf!?\xfd\xd77\x01\x80;t\x1f\t\x0eu\xda?$\x01\x80\x9f\xe8\x9e\t\x1c\x1b\x01\x80\xdftL!\x10\x00\xf8\x05\xc7\xb4\xe9\xbb|\x1f\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@0\x01\x80`\x02\x00\xc1\x04\x00\x82\t\x00\x04\x13\x00\x08&\x00\x10L\x00 \x98\x00@\xb0Q\x1fC\x9b\xa6\xe9c,\xb0e}\xec\xd4g=\xcc\x04\xbey\xb3\xeb\x05\x00\x00\x00\x07\xeb\x7f\xc3\xf3Z\x80-\xb2\xc5>\x00\x00\x00\x00IEND\xaeB`\x82'
DEFAULT_IMAGE = Image.open(io.BytesIO(DEFAULT_IMAGE_DATA))
DEFAULT_IMAGE_TYPE = AtomDataType.PNG

DEFAULT_FILE_EXTENSION = "m4a"
IMAGE_WIDTH=256
IMAGE_HEIGHT=256


class MultiStringVars:
    """
    A class made to de-duplicate the logic for having an arbitrary number
    of separate editable fields in one view
    """
    def __init__(self, main_container, under_widget=None):
        self.container = ttk.Frame(main_container)
        self.under_widget = under_widget

        self.vars = []
        self.var_entries = []
        self.new_entry_button = None

    def reset_tab_order(self):
        """
        Resets the entire tab order to be what it should

        I honestly don't know which way `lift`/`lower` work i just adjusted
        them until they did
        """
        if self.var_entries:
            prev_frame, prev_entry, prev_button = self.var_entries[0]
            self.under_widget.lower(prev_entry)
            prev_entry.lower(prev_button)

        for frame, cur_entry, cur_button in self.var_entries[1:]:
            prev_frame.lower(cur_entry)
            cur_entry.lower(cur_button)

            prev_frame = frame
            prev_button = cur_button

        if self.new_entry_button:
            if self.var_entries:
                self.new_entry_button.lift(prev_button)
            else:
                self.under_widget.lower(self.new_entry_button)

    def add_button(self):
        self.new_entry_button = ttk.Button(
            self.container,
            text="+",
            command=self.add_new_entry
        )
        self.new_entry_button.pack(side="bottom", fill="x")

        self.reset_tab_order()

    def set(self, strings):
        for child in self.container.winfo_children():
            child.destroy()

        self.vars = []
        self.var_entries = []
        for st in strings:
            var = StringVar()
            var.set(st)
            self.vars.append(var)
            self.var_entries.append(self.generate_new_entry(var))

        self.add_button()

    def get(self):
        return [var.get() for var in self.vars]

    def generate_new_entry(self, text_var):
        new_frame = ttk.Frame(self.container)
        new_frame.pack(side="top", fill="x")

        text_entry = ttk.Entry(new_frame, textvariable=text_var)
        text_entry.grid(column=0, row=0, sticky=(E, W))
        del_button = ttk.Button(new_frame,
            text="-",
            width=3,
            command=self.delete_specific_entry(text_var, new_frame)
        )
        del_button.grid(column=1, row=0)

        new_frame.columnconfigure(0, weight=1)

        return new_frame, text_entry, del_button

    def add_new_entry(self):
        text_var = StringVar()

        self.vars.append(text_var)
        self.var_entries.append(self.generate_new_entry(text_var))
        self.reset_tab_order()

    def delete_specific_entry(self, var, entry):
        """
        Returns a function that deletes a specific entry
        """
        def _delete_helper():
            entry.pack_forget()
            entry.destroy()

            # Remove entry from var_entries
            self.var_entries = [
                (frame, t, d) for frame, t, d in self.var_entries
                if frame != entry
            ]
            self.vars.remove(var)

        return _delete_helper

    def delete_last_entry(self):
        i = len(self.var_entries)-1
        if i >= 0:
            self.delete_specific_entry(variables[i], entries[i])()


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
        self.image_type = DEFAULT_IMAGE_TYPE
        self.image = ImageTk.PhotoImage(DEFAULT_IMAGE)

        self.image_button = ttk.Button(image_container,
            image=self.image,
            command=self.set_image_leftclick)
        self.image_button.bind(
            "<Button-2>",
            lambda _: self.set_image_rightclick()
        )
        self.image_button.bind(
            "<Button-3>",
            lambda _: self.set_image_rightclick()
        )
        self.image_button.grid(column=0, row=0)

        main_container = ttk.Frame(container)
        main_container.grid(column=1, row=r, sticky=(N, W, E, S))

        self.filename = StringVar()
        self.title = StringVar()
        self.album = StringVar()
        self.year = StringVar()

        self.artists = MultiStringVars(main_container)
        self.album_artists = MultiStringVars(main_container)
        self.genres = MultiStringVars(main_container)

        ttk.Label(main_container, text="Filename:")\
           .grid(column=0, row=0)
        ttk.Label(main_container, textvariable=self.filename)\
           .grid(column=1, row=0, sticky=(W, E))

        ttk.Label(main_container, text="Title:")\
           .grid(column=0, row=1)
        self.title_entry = ttk.Entry(main_container, textvariable=self.title)
        self.title_entry.grid(column=1, row=1, sticky=(W, E))

        self.artists.under_widget =  self.title_entry
        ttk.Label(main_container, text="Artists:")\
            .grid(column=0, row=2, sticky=N)
        self.artists.container.grid(column=1, row=2, sticky=(N, S, E, W))

        ttk.Label(main_container, text="Album:")\
           .grid(column=0, row=3)
        self.album_entry = ttk.Entry(main_container, textvariable=self.album)
        self.album_entry.grid(column=1, row=3, sticky=(W, E))

        self.album_artists.under_widget = self.album_entry
        ttk.Label(main_container, text="Album Artists:")\
            .grid(column=0, row=4, sticky=N)
        self.album_artists.container.grid(column=1, row=4, sticky=(N, S, E, W))

        ttk.Label(main_container, text="Year:")\
           .grid(column=0, row=5)
        self.year_entry = ttk.Entry(main_container, textvariable=self.year)
        self.year_entry.grid(column=1, row=5, sticky=(W, E))

        self.genres.under_widget = self.year_entry
        ttk.Label(main_container, text="Genres:")\
           .grid(column=0, row=6, sticky=N)
        self.genres.container.grid(column=1, row=6, sticky=(N, S, E, W))

        for msv in (self.artists, self.album_artists, self.genres):
            msv.add_new_entry()
            msv.add_button()

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(0, weight=1)

        image_container.columnconfigure(0, weight=1)
        image_container.rowconfigure(0, weight=1)

        main_container.columnconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=4)
        self.artists.container.columnconfigure(0, weight=1)
        self.album_artists.container.columnconfigure(0, weight=1)
        self.genres.container.columnconfigure(0, weight=1)

        self.image_search_directory = os.getcwd()

    def load_from_song(self, song):
        if song is not None:
            self.filename.set(song.filename)
            self.title.set(song.title)
            self.album.set(song.album)
            self.year.set(song.year)

            self.artists.set(song.artists)
            self.album_artists.set(song.album_artists)
            self.genres.set(song.genres)

            self.image_data = song.image_data
            self.image_type = song.image_type
            self.update_image()
        else:
            self.filename.set("No File Loaded!")
            self.title.set("")
            self.album.set("")
            self.year.set("")

            self.artists.set([""])
            self.album_artists.set([""])
            self.genres.set([""])

            self.image_data = None
            self.image_type = DEFAULT_IMAGE_TYPE
            self.update_image()


    def save_to_song(self, song):
        song.title = self.title.get()
        song.album = self.album.get()
        song.year = self.year.get()

        song.artists = self.artists.get()
        song.album_artists = self.album_artists.get()
        song.genres = self.genres.get()

        song.image_data = self.image_data
        song.image_type = self.image_type

        song.refresh()

    def set_image_leftclick(self):
        filename = filedialog.askopenfilename(
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpeg, *.jpg"), ("All Files", "*.*")],
            title="Choose Album Art File",
            initialdir = self.image_search_directory
        )
        self.load_image_from_file(filename, update_search=True)
        self.update_image()

    def set_image_rightclick(self):
        url = simpledialog.askstring(
            "Load Image URL",
            "Enter a URL to load album artwork from:"
        )

        if url:
            self.image_data, self.image_type = load_image_from_url(url)
            self.update_image()

    def load_image_from_file(self, filename=None, update_search=False):
        if filename is not None and \
           os.path.exists(filename) and os.path.isfile(filename):
            if filename.lower().endswith('png'):
                self.image_type = AtomDataType.PNG
            else:
                self.image_type = AtomDataType.JPEG

            with open(filename, 'rb') as f:
                self.image_data = f.read()

            if update_search:
                self.image_search_directory = os.path.dirname(filename)
        else:
            self.image_data = None

    def update_image(self):
        if self.image_data:
            self.image = ImageTk.PhotoImage(
                Image.open(io.BytesIO(self.image_data))\
                     .resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
            )
        else:
            self.image = ImageTk.PhotoImage(DEFAULT_IMAGE)
        self.image_button.configure(image=self.image)


class SongLoader:
    def __init__(self, container, indexvar, callbacks=[]):
        self.base_directory = os.getcwd()
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
            initialdir=self.base_directory
        )
        if directory:
            self.base_directory = directory
            self.refresh_filelist()

    def refresh_filelist(self):
        unfiltered_list = os.listdir(self.base_directory)
        self.file_list = [filename for filename in unfiltered_list \
            if filename.endswith(DEFAULT_FILE_EXTENSION)]

        if len(self.file_list) == 0:
            # Loaded a directory w/ no songs
            self.current_index = None
            self.update_current_song(None)
        elif self.current_index is None:
            # Loaded a directory w/ songs, coming from one w/o any songs
            self.current_index = 0
            self.load_song(self.file_list[0])

        self.refresh_indexvar()

    def load_song(self, filename):
        filepath = os.path.join(self.base_directory, filename)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            song = Song(filepath)
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

        if new_index and 0 <= new_index < len(self.file_list):
            self.current_index = new_index
            self.load_song(self.file_list[new_index])
            self.refresh_indexvar()
        else:
            simpledialog.SimpleDialog(
                root,
                text=USAGE_TEXT,
                buttons=["Ok"],
                title="Usage Dialog"
            ).go()

    def dialog_load_song(self):
        filename = filedialog.askopenfilename(
            filetypes=[
                (DEFAULT_FILE_EXTENSION.upper(), "*."+DEFAULT_FILE_EXTENSION),
                ("All Files", "*.*")
            ],
            title="Choose Song",
            initialdir=os.getcwd()
        )

        if filename:
            self.base_directory = os.path.dirname(filename)
            song_filename = os.path.basename(filename)

            # Mostly copied from self.refresh_filelist(), but too many
            # modifications needed to be made if I were to re-use directly
            unfiltered_list = os.listdir(self.base_directory)
            self.file_list = [filename for filename in unfiltered_list \
                if filename.endswith(DEFAULT_FILE_EXTENSION)]

            new_index = self.file_list.index(song_filename)
            self.current_index = new_index
            self.load_song(self.file_list[new_index])
            self.refresh_indexvar()

    def increment_index(self):
        self.refresh_filelist()
        if self.current_index is not None:
            self.current_index = (self.current_index + 1) % len(self.file_list)
            self.load_song(self.file_list[self.current_index])
            self.refresh_indexvar()

    def decrement_index(self):
        self.refresh_filelist()
        if self.current_index is not None:
            self.current_index = (self.current_index - 1) % len(self.file_list)
            self.load_song(self.file_list[self.current_index])
            self.refresh_indexvar()

    def refresh_indexvar(self):
        if self.current_index is None:
            self.indexvar.set("0 / 0")
        else:
            self.indexvar.set(f"{self.current_index + 1} / {len(self.file_list)}")


class MetadataGuesser:
    def __init__(self, songloader):
        self.handler = ScrapeHandler()
        self.handler.register(SpotifyScraper(), r"open\.spotify\.com")
        self.songloader = songloader

    def url_load_metadata(self):
        text = simpledialog.askstring(
            "Load Metadata",
            "Enter a URL to load metadata from:"
        )

        if text:
            song = self.songloader.current_song
            if self.handler.handle(text, song):
                self.songloader.update_current_song(song)

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

    metadataguesser = MetadataGuesser(songloader)

    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open File", command=songloader.dialog_load_song)
    filemenu.add_command(label="Open Directory", command=songloader.set_directory)
    filemenu.add_command(label="Set Index", command=songloader.set_index)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Guess Metadata", command=lambda: print("Not Implemented!"))
    editmenu.add_command(label="Load Metadata from URL", command=metadataguesser.url_load_metadata)
    editmenu.add_command(label="Refresh Directory", command=songloader.refresh_filelist)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    USAGE_TEXT = """USAGE:

Ctrl+o: Open a song to edit metadata of
Ctrl+Shift+o: Open a directory to edit metadata of songs in
Ctrl+k: Load the song's metadata from a URL
 * Only Spotify song urls supported at the moment
Ctrl+r: Refresh listing of songs in the directory
Ctrl+s: Save metadata for the current song
 * If you make a mistake, just close the program or toggle which song you're on,
   nothing is saved until you manually click save.
"""
    HELP_TEXT = """CopyLeft 2021, PolyWolf. Find me on Discord!"""
    helpmenu.add_command(
        label="Usage",
        command=lambda: simpledialog.SimpleDialog(
            root,
            text=USAGE_TEXT,
            buttons=["Ok"],
            title="Usage Dialog"
        ).go()
    )
    helpmenu.add_command(
        label="About",
        command=lambda: simpledialog.SimpleDialog(
            root,
            text=HELP_TEXT,
            buttons=["Ok"],
            title="Help Dialog"
        ).go()
    )
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

    root.bind("<Control-s>", lambda _: full_save())
    root.bind("<Control-o>", lambda _: songloader.dialog_load_song())
    root.bind("<Control-O>", lambda _: songloader.set_directory())
    root.bind("<Control-k>", lambda _: metadataguesser.url_load_metadata())
    root.bind("<Control-r>", lambda _: songloader.refresh_filelist())

    root.config(menu=menubar)
    root.geometry("640x480")
    root.mainloop()

if __name__ == "__main__":
    main()
