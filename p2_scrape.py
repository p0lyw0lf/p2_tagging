from io import BytesIO
import re
from urllib.request import urlopen

from PIL import Image
from mutagen.mp4 import AtomDataType


class Scraper:
    def __init__(self):
        pass

    def scrape(self, url, song):
        raise NotImplementedError


class ScrapeHandler:
    def __init__(self):
        self.scrapers = []

    def register(self, scraper, regex):
        if not isinstance(scraper, Scraper):
            raise TypeError("Argument 'scraper' must subclass class 'Scraper'")

        self.scrapers.append((re.compile(regex), scraper))

    def handle(self, text, song):
        for regex, scraper in self.scrapers:
            if regex.search(text):
                return scraper.scrape(text, song)
        return False

def load_image_from_url(url):
    """
    This is used in enough places, why not add it here?

    Loads image_data from the url, normalizing to a PNG image_type
    """
    img = Image.open(urlopen(url))
    output_fp = BytesIO()
    img.save(output_fp, format="PNG")

    image_data = output_fp.getvalue()
    image_type = AtomDataType.PNG

    return image_data, image_type
