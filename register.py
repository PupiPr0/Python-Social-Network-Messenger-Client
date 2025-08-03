import requests

def register(username, fullname, password, email, referrer=None):
    url = 'https://api.dkon.app/api/v2/method/account.signUp'
    data = {
        'clientId': '1302',
        'hash': 'U2F5YSBzdWthIGtldGlrYSBBbGV4YSBtZW5pZHVyaSBzYXlh',
        'appType': '1',
        'username': username,
        'fullname': fullname,
        'password': password,
        'email': email,
        'referrer': referrer
    }
    
    response = requests.post(url, data=data)
    return response.json()
