#!/usr/bin/python
import json
import ipaddress
import urllib.request

URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

# aws ip range calculate
response = urllib.request.urlopen(URL)
data = json.loads(response.read())

mtl = open("mikrotikaws.txt", "w")

for reg in data['prefixes']:
    if reg['region'] == 'us-west-1':      # change region depending on your preference ("us-west-1")
        ip = ipaddress.ip_network(reg['ip_prefix'])
        mtrule = "do { /ip firewall address-list add address=" + str(ip) + " list=AWS } on-error={}\n"
        mtl.write(mtrule)
mtl.close()
print("Done")
