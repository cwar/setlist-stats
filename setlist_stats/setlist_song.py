# song.py

class SetlistSong:
    def __init__(self, song_data):
        print(f"song_data is {song_data}")
        self.footnote = song_data.get("footnote")
        self.isjam = song_data.get("isjam")
        self.isjamchart = song_data.get("isjamchart")
        self.isoriginal = song_data.get("isoriginal")
        self.isreprise = song_data.get("isreprise")
        self.isverified = song_data.get("isverified")
        self.jamchart_notes = song_data.get("jamchart_notes")
        self.original_artist = song_data.get("original_artist")
        self.permalink = song_data.get("permalink")
        self.position = song_data.get("position")
        self.notes = song_data.get("shownotes")
        self.slug = song_data.get("slug")
        self.song_id = song_data.get("song_id")
        self.songname = song_data.get("songname")
        self.soundcheck = song_data.get("soundcheck")
        self.tour_id = song_data.get("tour_id")
        self.transition = song_data.get("transition")
        self.transition_id = song_data.get("transition_id")
        self.uniqueid = song_data.get("uniqueid")

    def __str__(self):
        return f"SetlistSong: {self.songname} by {self.artist}"
