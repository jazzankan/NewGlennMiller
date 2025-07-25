import requests

def feed_it(artist, date):
    # Utvecklingsurl. OBS place_id och organizer_id måste ändras beroende på miljö. Skarpa: 1 resp 32
    #url = 'http://localhost/api/v1/events'
    #Nyckel utvecklingsmiljön: 2|MDybuSA2L23uICjpYchwoqF07enRpwvuuiYD11Y32f517b7a
    url = 'https://jazztider.webbsallad.se/api/v1/events'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization':  "Bearer " + '2|CYXAKvuNNEnSlAiy2BgvkPaimuIwXGVMZDMT37M69b25751f', 'accept': 'application/json'}
    data = {'name': artist, 'place_id': '1', 'organizer_id': '32', 'day': date,'timeofday': '20.00', 'link': 'https://www.glennmillercafe.se/konserter'}
    requests.post(url,headers=headers, data=data)