import requests

def request_api_data(query_char): 
    url = 'http://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try agian')

def pwned_api_check(password): 
    #check pass if it exists in API response
    pass

request_api_data('CBFDA')