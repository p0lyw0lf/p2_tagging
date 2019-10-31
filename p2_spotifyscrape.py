import spotipy

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
        
        # TODO: set image. this should be fairly easy, just need to download image and
        # add capability to Song to check what format (PNG or JPEG) it is.
        
        return True
        