# setlist.py

from setlist_song import SetlistSong

class Setlist:
    def __init__(self, setlist_data):
        self.artist = setlist_data[0].get("artist")
        self.artist_id = setlist_data[0].get("artist_id")
        self.settype = setlist_data[0].get("settype")
        self.setnumber = setlist_data[0].get("setnumber")
        self.songs = [SetlistSong(song_data) for song_data in setlist_data]

    def __str__(self):
        return f"Setlist (Set {self.setnumber}, Type: {self.settype}) with {len(self.songs)} songs"

class Setlists:
    def __init__(self, setlists_data):
        self.setlists = [Setlist(setlist_data) for setlist_data in setlists_data]