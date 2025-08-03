import requests

def login(username, password):
    url = 'https://api.dkon.app/api/v3/method/account.signIn'
    data = {
        'clientId': '1302',
        'username': username,
        'password': password
    }
    
    response = requests.post(url, data=data)
    return response.json()
