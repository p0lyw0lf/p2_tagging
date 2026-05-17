import os
import subprocess
from typing import List, Dict, Tuple

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, PictureType, Encoding
from mutagen.id3 import TIT2, TPE1, TALB, TPE2, TDRC, APIC


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
                 year: str = ""):
        self.title = title
        self.artists = artists
        self.album = album
        self.album_artists = album_artists
        self.year = year

        self.source_filename = source_filename
        self.music_output_directory = os.path.dirname(source_filename)
        self.filename = os.path.basename(self.source_filename)
        self.image_filename = None
        self.image_type = "image/png"
        self.image_data = b''

        self._read_tags_from_MP3(MP3(self.source_filename))

    def _image_extension(self):
        if self.image_type == "image/png":
            return "png"
        elif self.image_type == "image/jpeg":
            return "jpeg"
        else:
            raise ValueError(
                "Got incorrect image type {} while loading".format(
                    self.image_type))

    def refresh(self):
        self.artists_string = artist_list(self.artists)
        self.album_artists_string = artist_list(self.album_artists)

    def save_tags(self):
        f = MP3(os.path.join(self.music_output_directory, self.filename))
        if f.tags is None:
            f.tags = ID3()

        f.tags.setall("TIT2", [TIT2(text=self.title)])
        f.tags.setall("TPE1", [TPE1(text=self.artists_string)])
        f.tags.setall("TALB", [TALB(text=self.album)])
        f.tags.setall("TPE2", [TPE2(text=self.album_artists_string)])
        f.tags.setall("TDRC", [TDRC(text=self.year)])

        if self.image_data:
            f.tags.setall("APIC", [APIC(
                mime_type=self.image_type,
                type=PictureType.COVER_FRONT,
                data=self.image_data,
            )])

        f.save()

    def _read_tags_from_MP3(self, f):
        if f.tags is None:
            return

        self.title = fst_or_empty(f.tags.getall("TIT2"))
        self.artists_string = fst_or_empty(f.tags.getall("TPE1"))
        self.artists = list_from_artists(self.artists_string)
        self.album = fst_or_empty(f.tags.getall("TALB"))
        self.album_artists_string = fst_or_empty(f.tags.getall("TPE2"))
        self.album_artists = list_from_artists(self.album_artists_string)
        self.year = fst_or_empty(f.tags.getall("TDRC"))

        images = f.tags.getall("APIC")
        self.image_data = None
        for image in images:
            if isinstance(image, APIC):
                if self.image_data is None or self.image_data.type != PictureType.COVER_FRONT:
                    self.image_data = image

        if self.image_data:
            self.image_type = self.image_data.mime
            self.image_data = self.image_data.data

    def read_tags(self):
        f = MP3(os.path.join(self.music_output_directory, self.filename))
        self._read_tags_from_MP3(f)


def fst_or_empty(tags):
    if len(tags) > 0:
        tag = tags[0]
        return tag.text[0]
    else:
        return ""
