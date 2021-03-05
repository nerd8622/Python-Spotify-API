import requests

def safeGet(url, params, headers):
    try:
        response = requests.get(url=url, params=params, headers=headers).json()
        return response
    except Exception as e:
        print(f"AHHHHHHHH:\n {e}")
        return False
