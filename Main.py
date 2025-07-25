import time
from bs4 import BeautifulSoup
import requests
from feedAPI import feed_it

response = requests.get("https://www.glennmillercafe.se/konserter")
glenn_page = response.text
months = ['januari', 'Januari', 'februari', 'Februari', 'mars', 'Mars','april', 'April', 'maj', 'Maj', 'juni', 'Juni','juli','Juli','augusti', 'Augusti', 'september', 'September', 'oktober', 'Oktober', 'november','November', 'december', 'December']
found_months = []
month_index = []

print(glenn_page)
"""
for m in months:
    try:
        month_index.append(glenn_page.index(m))
        found_months.append(m)
    except(ValueError):
        pass
greatest_index = month_index.index(max(month_index))
latest_month = found_months[greatest_index]
print(f"Senaste månaden är { latest_month }:")

glenn_page = glenn_page[month_index[-1]:]

soup = BeautifulSoup(glenn_page, "html.parser")
artist_clean = []
date_clean = []
artists = soup.find_all("p", class_="artist")
for a in artists:
    artist_text = a.get_text()
    artist_clean.append(artist_text)
    print(artist_text)

dates = soup.find_all("p", class_="date")
for d in dates:
    date_text = d.get_text()
    date_clean.append(date_text)

if len(artist_clean) != len(date_clean):
    print("\nDiskrepans mellan artister och datum!")
else:
    user_input = input("Vill du mata in posterna? j/n:\n")
    if user_input == "j":
        artist_index = 0
        date_index = 0
        for ac in artist_clean:
            feed_it(artist_clean[artist_index], date_clean[date_index])
            print(artist_clean[artist_index])
            artist_index += 1
            date_index += 1
            time.sleep(0.5)
"""