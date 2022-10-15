from datetime import datetime
import re
from urllib.request import urlopen, Request
from functools import lru_cache
from bs4 import BeautifulSoup
from .scrape import Scraper, load_image_from_url
"""
Logic ported from
https://github.com/DevAndromeda/soundcloud-scraper/blob/master/src/util/Util.js#L179
"""

SOUNDCLOUD_BASE_URL = "https://soundcloud.com"
SOUNDCLOUD_SCRIPT_ELEMENT_REGEX = re.compile(
    r'<script( crossorigin)? src="(.*?)"')
SOUNDCLOUD_CLIENT_ID_KEY_REGEX = re.compile(r'client_id:"(.*?)"')
SOUNDCLOUD_GENRE_KEY_REGEX = re.compile(r',"genre":"(.*?)","')

SOUNDCLOUD_FETCH_HEADERS = {
    "User-Agent": """\
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/81.0.4044.129 Safari/537.36""",
    "Accept": "*/*",
    "Accept-Encoding": "identity",
}


def request(url: str) -> str:
    return urlopen(Request(
        url, headers=SOUNDCLOUD_FETCH_HEADERS)).read().decode('utf-8')


def _get_soundcloud_key(url: str) -> str:
    html = request(url)
    for match in SOUNDCLOUD_SCRIPT_ELEMENT_REGEX.finditer(html):
        js_url = match.group(2)
        js = request(js_url)
        if match := SOUNDCLOUD_CLIENT_ID_KEY_REGEX.search(js):
            key = match.group(1)
            return key


@lru_cache
def get_soundcloud_key() -> str:
    return _get_soundcloud_key(SOUNDCLOUD_BASE_URL)


class SoundcloudScraper(Scraper):

    def scrape(self, url, song):
        raw_html = request(url)
        if match := SOUNDCLOUD_GENRE_KEY_REGEX.search(raw_html):
            song.genres = [match.group(1)]
        else:
            song.genres = []

        html = BeautifulSoup(raw_html, 'html5lib')

        song.title = html.select_one('meta[property="og:title"]')['content']
        song.album = song.title
        song.artists = [
            html.select_one('h1[itemprop="name"]').select('a')[1].string
        ]
        song.album_artists = song.artists
        song.image_data, song.image_type = load_image_from_url(
            html.select_one('meta[property="og:image"]')['content'])
        song.year = str(
            datetime.strptime(
                html.select_one('header').select_one('time').string,
                "%Y-%m-%dT%H:%M:%SZ").year)

        return True


if __name__ == "__main__":
    client_id = get_soundcloud_key()
    print(f"{client_id=}")

    class Printer:

        def __init__(self):
            self.data = dict()

        def __setattr__(self, name, value):
            print(name, value)
            self.__dict__[name] = value

    SoundcloudScraper().scrape(
        "https://soundcloud.com/user-655155237/strawberry-godzilla-sugar-co",
        Printer())
