import re

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