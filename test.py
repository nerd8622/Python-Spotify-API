from spotify_api import API

token = open('token.txt', 'r').read()

api = API(token)
print(api.currentUser())
