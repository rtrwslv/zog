import requests

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params={'what': 'chart'}, timeout=5)
chart = response.json()['chartPositions']
for track in chart:
    place = track['track']['chart']['position']
    name = track['track']['title']
    author = []
    artists = track['track']['artists']
    for i in range(min(len(artists), 10)):
        author.append(artists[i]['name'])
    with open('chart.txt', 'a') as f:
        print(f"{place}: {author}: {name}", file=f)
