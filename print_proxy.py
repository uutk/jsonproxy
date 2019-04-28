import requests,json

r=requests.get('https://raw.githubusercontent.com/rachitkataria13/jsonproxy/master/proxy.json')
r_json=r.json()

r_len = len(r_json['data'])
#printing all ip's
for i in range(r_len):
        print(r_json['data'][i])

print("There Are",r_len,"Proxies Available")
