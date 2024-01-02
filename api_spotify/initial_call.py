import requests
from tokens import AUTH_TOKEN
from spotify_api import *

class GetPlaylistError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'There was an error retrieving your playlist.'

def get_playlist(playlist_id: str = None):
    headers = {
        'Authorization': 'Bearer ' + AUTH_TOKEN
    }
    if playlist_id is None:
        playlist_url = get_playlist_input()
    else:
        playlist_url = get_playlist(playlist_id)
    
    response = requests.get(playlist_url, headers = headers)

    if response.status_code == 200:
        body = response.json()
        #print(body)
        return body
    else:
        raise GetPlaylistError
    
def get_tracks(playlist: dict):
    for x in playlist["tracks"]["items"]:
        all_data = x['track']

        track_name = all_data['name']
        artist_name = all_data['artists'][0]['name']
        album_name = all_data['album']['name']

        print('{} by {} from {}'.format(track_name, artist_name, album_name))


def main():
    playlist = get_playlist()
    get_tracks(playlist)

if __name__ == '__main__':
    main()