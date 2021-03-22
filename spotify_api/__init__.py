from .web_requests import safeGet


class API:
    def __init__(self, token):
        self.url = lambda s: f"https://api.spotify.com/v1/{s}"
        self.authHeader = {'Authorization': f'Bearer {token}'}

    def get_album_tracks(self, a_id):
        response = safeGet(self.url(f'albums/{a_id}/tracks'), {}, self.authHeader)
        return response

    def get_user(self, uid):
        return User(self, uid)
    
    def currentUser(self):
        response = safeGet(self.url('me'), {}, self.authHeader)
        return response


class Track:
    def __init__(self, api, data, features):
        self.api = api
        self.tid = data['track']['id']
        self.url = f"https://api.spotify.com/v1/tracks/{self.tid}"
        self.name = data['track']['name']
        self.explicit = data['track']['explicit']
        self.raw = data
        self.features = features
        self.tempo = features['tempo']

class Playlist:
    def __init__(self, api, data):
        self.api = api
        self.pid = data['id']
        self.url = lambda s: f"https://api.spotify.com/v1/playlists/{self.pid}/{s}"
        self.featuresUrl = "https://api.spotify.com/v1/audio-features"
        self.name = data['name']
        self.raw = data

    def get_tracks(self):
        response = safeGet(self.url('tracks'), {'market': 'US'}, self.api.authHeader)
        features = safeGet(self.featuresUrl, {'ids': ','.join(i['track']['id'] for i in response["items"])}, self.api.authHeader)
        return [Track(self.api, item, feature) for item, feature in zip(response['items'], features['audio_features'])]

    
class User:
    def __init__(self, api, uid):
        self.api = api
        self.url = lambda s: f"https://api.spotify.com/v1/users/{uid}/{s}"
        self.uid = uid
        self.raw = safeGet(self.url(''), {}, self.api.authHeader)
        self.name = self.raw['display_name']


    def get_playlists(self):
        response = safeGet(self.url('playlists'), {}, self.api.authHeader)
        return [Playlist(self.api, item) for item in response['items']]

    
