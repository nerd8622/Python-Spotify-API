from spotify_api import API

token = open('token.txt', 'r').read()

api = API(token)

targetUser = api.get_user(input("Enter User ID: "))
playlists = targetUser.get_playlists()
print()
for i in range(len(playlists)):
    print(f"{i}: {playlists[i].name}")
print()
playlist = playlists[int(input("Make Selection: "))]
tracks = playlist.get_tracks()
songs = sorted([[t.tempo, t.name] for t in tracks])
songs.reverse()
print()
for song in songs[:min(len(songs),int(input("Max to show: ")))]:
    print(f"{song[1]} ({song[0]})")
