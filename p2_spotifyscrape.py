import spotipy
from mutagen.mp4 import AtomDataType

from p2_scrape import Scraper, load_image_from_url
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

        song.image_data, song.image_type = load_image_from_url(
            track['album']['images'][0]['url']
        )
        song.refresh()

        return True

