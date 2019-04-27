import requests,json
r=requests.get('https://raw.githubusercontent.com/rachitkataria13/jsonproxy/master/proxy.json')
r_json=r.json()
print(len(r_json['dat']))
