import os
import subprocess
from typing import List, Dict, Tuple

from mutagen.mp4 import AtomDataType, MP4, MP4Cover


def _lev(a: str, b: str, i: int, j: int, d: Dict[Tuple[int, int], int]) -> int:
    if (i, j) in d:
        return d[i, j]
    if min(i, j) == 0:
        d[i, j] = max(i, j)
        return d[i, j]
    p1 = lev(a, b, i - 1, j, d) + 1
    p2 = lev(a, b, i, j - 1, d) + 1
    p3 = lev(a, b, i - 1, j - 1, d) + (0 if a[i] == b[j] else 1)
    d[i, j] = min(p1, p2, p3)
    return d[i, j]


def lev(a: str, b: str) -> int:
    return _lev(a, b, len(a) - 1, len(b) - 1, dict())


def artist_list(names: List[str]) -> str:
    if len(names) > 2:
        out = ', '.join(names[:-2] + [''])
        out += names[-2] + ' & ' + names[-1]
    elif len(names) == 2:
        out = names[0] + ' & ' + names[1]
    elif len(names) == 1:
        out = names[0]
    else:
        out = ""

    return out


def list_from_artists(names: str) -> List[str]:
    parts = names.split(' & ')
    if len(parts) == 2:
        first, second = parts[0], parts[1]
        more_parts = first.split(', ')
        return more_parts + [second]
    else:
        # should be just one part in this case,
        # but account for weird stuff happening anyways
        return parts


UNSAFE_CHARS = "/\\?|:"


def safe_windows_filename(f: str) -> str:
    for ch in UNSAFE_CHARS:
        if ch in f:
            f = f.replace(ch, "")
    return f


class Song:
    """
    A data class to help abstract away the P2 tagging mechanism
    into a nicer interface.

    Example usage:

    filename = os.path.join(os.getcwd(), "example.mp4")
    s = Song(filename)
    s.read_tags()
    s.artists = ["BLU J"]
    s.year = "2019"
    s.refresh()
    s.save_tags()
    """

    def __init__(self,
                 source_filename: str,
                 title: str = "",
                 artists: List[str] = [],
                 album: str = "",
                 album_artists: List[str] = [],
                 year: str = "",
                 genre: str = ""):
        self.title = title
        self.artists = artists
        self.album = album
        self.album_artists = album_artists
        self.year = year
        self.genre = genre

        self.source_filename = source_filename
        self.music_output_directory = os.path.dirname(source_filename)
        self.filename = os.path.basename(self.source_filename)
        self.image_filename = None
        self.image_type = AtomDataType.PNG
        self.image_data = b''

        self._read_tags_from_MP4(MP4(self.source_filename))

    def _image_extension(self):
        if self.image_type == AtomDataType.PNG:
            return "png"
        elif self.image_type == AtomDataType.JPEG:
            return "jpeg"
        else:
            raise ValueError(
                "Got incorrect image type {} while loading".format(
                    self.image_type))

    def refresh(self):
        self.artists_string = artist_list(self.artists)
        self.album_artists_string = artist_list(self.album_artists)

        new_filename = safe_windows_filename(
            f"{self.artists_string}_{self.title}_{self.album}.m4a")

        if new_filename != self.filename:
            old_filepath = os.path.join(self.music_output_directory,
                                        self.filename)
            new_filepath = os.path.join(self.music_output_directory,
                                        new_filename)
            if os.path.exists(old_filepath) and os.path.isfile(old_filepath):
                os.rename(old_filepath, new_filepath)
            else:
                # we need to create the M4A file to tag
                # this assume ffmpeg is on the $PATH
                cmd = [
                    "ffmpeg", "-y", "-i", self.source_filename, "-vn",
                    new_filepath
                ]
                print("Creating new file")
                print(subprocess.run(cmd))
            self.filename = new_filename

    def save_tags(self):
        f = MP4(os.path.join(self.music_output_directory, self.filename))
        f.tags[u'\xa9nam'] = self.title
        f.tags[u'\xa9ART'] = self.artists_string
        f.tags[u'\xa9alb'] = self.album
        f.tags[u'aART'] = self.album_artists_string
        f.tags[u'\xa9day'] = self.year
        f.tags[u'\xa9gen'] = self.genres

        if self.image_data:
            f.tags[u'covr'] = [MP4Cover(self.image_data, self.image_type)]
        f.save()

    def _read_tags_from_MP4(self, f):
        self.title = f.tags.get(u'\xa9nam', [''])[0]
        self.artists_string = f.tags.get(u'\xa9ART', [''])[0]
        self.artists = list_from_artists(self.artists_string)
        self.album = f.tags.get(u'\xa9alb', [''])[0]
        self.album_artists_string = f.tags.get(u'aART', [''])[0]
        self.album_artists = list_from_artists(self.album_artists_string)
        self.year = f.tags.get(u'\xa9day', [''])[0]
        self.genres = f.tags.get(u'\xa9gen', [''])

        self.image_data = f.tags.get(u'covr',
                                     [MP4Cover(b'', self.image_type)])[0]
        if self.image_data:
            self.image_type = self.image_data.imageformat

    def read_tags(self):
        f = MP4(os.path.join(self.music_output_directory, self.filename))
        self._read_tags_from_MP4(f)
