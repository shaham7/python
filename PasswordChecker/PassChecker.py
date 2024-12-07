import requests
import hashlib

def request_api_data(query_char): 
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    print(res.status_code)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try agian')

def pwned_api_check(password):
    sha1password = hashlib.sha1(
        password.encode('utf-8')
    ).hexdigest().upper()
    print(sha1password)

pwned_api_check('password123')