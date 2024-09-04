# main.py

import requests
from datetime import datetime
from show import Show



# Fetch the latest show data from the API
latest_setlist_response = requests.get("https://kglw.net/api/v2/latest.json?order_by=position&direction=asc")
latest_show_data = latest_setlist_response.json()['data']

# print(f"latest_show_data is {latest_show_data}")

# Extract the first show entry
show = Show(latest_show_data)
# print(f"{show}")

# Get the timezone based on city and country
timezone = show.get_timezone()
# print(f"timezone is {timezone}")

# Check if the show date is today
if True:
    print("The show is today!")
    print(show)
    show.print_setlists()
else:
    print(f"The show is not today ({datetime.now(timezone).strftime('%Y-%m-%d')}), it was on {show.showdate}")
