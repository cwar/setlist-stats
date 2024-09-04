# show.py

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
from setlist import Setlist
import pytz
from setlist_song import SetlistSong

class Show:
    def __init__(self, show_data):
        top_show_data = show_data[0]
        self.city = top_show_data.get("city")
        self.country = top_show_data.get("country")
        self.show_id = top_show_data.get("show_id")
        self.showdate = top_show_data.get("showdate")
        self.showtitle = top_show_data.get("showtitle")
        self.state = top_show_data.get("state")
        self.venue_id = top_show_data.get("venue_id")
        self.opener = top_show_data.get("opener")
        self.tourname = top_show_data.get("tourname")
        self.showorder = top_show_data.get("showorder")
        self.venuename = top_show_data.get("venuename")
        self.setlist = Setlist(show_data)

    def get_timezone(self):
        geolocator = Nominatim(user_agent="timezone_finder")
        location = geolocator.geocode(f"{self.city}, {self.country}")
        if location:
            tf = TimezoneFinder()
            timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
            print(f"{timezone_str}") if timezone_str else print("There was no timezone_str")
            return pytz.timezone(timezone_str) if timezone_str else pytz.utc
        else:
            return pytz.utc  # Default to UTC if location is not found

    def is_today(self, timezone):
        today = datetime.now(timezone).strftime('%Y-%m-%d')
        return self.showdate == today

    def print_setlists(self):
        print(f"self.setlists is {self.setlist}")
        for song in self.setlist.songs:
            line = f"#{song.position}: {song.songname}"
            if song.transition:
                line += f"{song.transition}"
            print(line)

    def __str__(self):
        return f"Tour: {self.tourname} Show: {self.showtitle} on {self.showdate} at {self.venuename}, {self.city}, {self.country}"
