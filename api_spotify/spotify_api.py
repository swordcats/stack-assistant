import requests

BASE_URL = "https://api.spotify.com/v1/"

def playlist_base():
    return BASE_URL + "playlists/"

def get_playlist(playlist_id: str):
    return playlist_base() + playlist_id + '?market=US'

def get_playlist_input():
    input_statement = "Please enter the ID of your playlist: "

    return get_playlist(input(input_statement))

__all__ = [playlist_base.__name__, get_playlist.__name__, get_playlist_input.__name__]