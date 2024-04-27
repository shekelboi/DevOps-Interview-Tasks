import requests
from collections import Counter

# Task 1
response = requests.get('https://api.discogs.com/artists/125246/releases')
data = response.json()
releases = data['releases']

# Task 2
between_1991_1992 = [r for r in releases if 1990 < r['year'] < 1993]
print(between_1991_1992)

# Task 3
artists = []
collaborations = []
for release in releases:
    current_artists = release['artist'].split(' / ')
    if len(current_artists) > 1:
        collaborations.append(release)
    artists.extend(release['artist'].split(' / '))
d = Counter(artists)
print(d.most_common(1)[0])
# print(sorted(d.items(), key=lambda t: t[1], reverse=True)[0])

#  Task 4
print(collaborations)
