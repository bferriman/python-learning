import requests

response_1 = requests.get("http://api.open-notify.org/astros.json")
print(response_1.json())

query = {
    'lat': '45',
    'lon': '180'
}
response_2 = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response_2.json())

# post / put examples
# response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# requests.put('https://httpbin.org/put', data = {'key':'value'})
