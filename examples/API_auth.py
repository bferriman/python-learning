import requests
from requests.auth import HTTPBasicAuth

# HTTP Basic Auth
res = requests.get(
    'https://api.github.com/user/',
    auth=HTTPBasicAuth('username', 'password')
)

print(res.json())

# with access tokens, like OAuth
# once you have a token...
my_headers = {'Authorization': 'Bearer {access_token'}
res = requests.get('http://httpbin.org/headers', headers=my_headers)

# using sessions to manage tokens
session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
res = session.get('https://httpbin.org/headers')