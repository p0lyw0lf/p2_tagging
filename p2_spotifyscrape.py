import spotipy
from io import BytesIO
from PIL import Image
from mutagen.mp4 import AtomDataType
from urllib.request import urlopen

from p2_scrape import Scraper
from p2_spotify_secret import ccm


# Create spotify client
#from spotipy.oauth2 import SpotifyClientCredentials
#ccm = SpotifyClientCredentials(client_id="<hex string>",
#                               client_secret="<hex string>")


class SpotifyScraper(Scraper):
    def __init__(self):
        self.sf = spotipy.Spotify(client_credentials_manager=ccm)
        
    def scrape(self, text, song):
        if not ('track' in text):
            print("Bad URL!")
            return False
        
        track = self.sf.track(text)
        
        song.title = track['name']
        song.artists = [artist['name'] for artist in track['artists']]
        song.album = track['album']['name']
        song.album_artists = [artist['name'] for artist in track['album']['artists']]
        song.year = track['album']['release_date'].split('-')[0]

        album = self.sf.album(track['album']['id'])
        song.genres = album['genres']
        
        song.refresh()
        
        rq = urlopen(track['album']['images'][0]['url'])
        img = Image.open(rq)
        output_fp = BytesIO()
        img.save(output_fp, format="PNG")

        song.image_type = AtomDataType.PNG
        song.write_image(output_fp.getvalue())
        
        return True
        
