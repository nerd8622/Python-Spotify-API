from spotify_api import API

token = open('token.txt', 'r').read()

api = API(token)

targetUser = api.get_user(input("Enter User ID: "))
playlists = targetUser.get_playlists()
print(f'Playlist Analysis for "{targetUser.name}":\n')
tot = []
for playlist in playlists:
    exp = []
    for track in playlist.get_tracks():
        exp.append(track.explicit)
        track.analyze()
        print(track.tempo)
    print(f'Playlist: {playlist.name}\n{exp.count(True)}/{len(exp)} ({exp.count(True)/len(exp)*100:.2f}%) Explicit!\n')
    tot.extend(exp)
print(f'User "{targetUser.name}" Total:\n{tot.count(True)}/{len(tot)} ({tot.count(True)/len(tot)*100:.2f}%) Explicit!')

