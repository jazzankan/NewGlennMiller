import time
from bs4 import BeautifulSoup
import requests
from feedAPI import feed_it

response = requests.get("https://www.glennmillercafe.se/konserter")
glenn_page = response.text
months = ['januari', 'Januari', 'februari', 'Februari', 'mars', 'Mars','april', 'April', 'maj', 'Maj', 'juni', 'Juni','juli','Juli','augusti', 'Augusti', 'september', 'September', 'oktober', 'Oktober', 'november','November', 'december', 'December']
found_months = []
month_index = []
artist_list = []
date_list = []
soup = BeautifulSoup(glenn_page, "html.parser")
soup = soup.main
for m in months:
    try:
        month_index.append(str(soup).index(m))
        found_months.append(m)
    except(ValueError):
        pass
greatest_index = month_index.index(max(month_index))
latest_month = found_months[greatest_index]
print(f"Senaste månaden är { latest_month }:")
glenn_page = str(soup)[month_index[-1]:]
soup = BeautifulSoup(str(glenn_page), "html.parser")
soup_artists = soup.find_all('p')
soup_dates = soup.find_all('h2')
for a in soup_artists:
    #En del datum är p och inte h2
    if not "20" in str(a):
        artist_list.append(a.text.strip())
    else:
        date_list.append(a.text.strip())

for d in soup_dates:
        date_list.append(d.text.strip())

date_list.sort()
if len(artist_list) != len(date_list):
    print("\nDiskrepans mellan artister och datum!")
else:
        for i in range(len(artist_list)):
            print(f"{artist_list[i]}, {date_list[i]}")
            user_input = input("Vill du mata in posten? j/n:\n")
            if user_input == "j":
                try:
                    feed_it(artist_list[i],date_list[i])
                    print("Posten inlagd.\n\n")
                except:
                    print(f"Misslyckad inmatning: {feed_it}")
