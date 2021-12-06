import pandas as pd
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import matplotlib.pyplot as plt



pd.set_option("display.max_columns",None)


auth_manager = SpotifyClientCredentials(client_id="89c9851f95df420fbe2ad1ec121dfb5b",
                                               client_secret="b37da3f962da459f9c86dc27eca24885")
sp = spotipy.Spotify(auth_manager= auth_manager)

results = sp.audio_features('https://open.spotify.com/track/6oVFpdtDzSgRLv8rUgFVUW?si=c1dbd00b4c644749')
print(results)