from web_requests import safeGet

class API:
    def __init__(self, token):
        self.url = lambda s: f"https://api.spotify.com/v1/{s}"
        self.authHeader = {'Authorization': f'Bearer {token}'}

    def get_album_tracks(self, a_id):
        response = safeGet(self.url(f'albums/{a_id}/tracks'), {}, self.authHeader)
        return response
    
    def currentUser(self):
        response = safeGet(self.url('me'), {}, self.authHeader)
        return response
