#import requests,json
from datetime import datetime
now = datetime.datetime.now()
time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
print(time_now)
#r=requests.get('http://sumanjay.ooo/jsonproxy/proxy.json')
#r_json=r.json()
#print(len(r_json['data']))
