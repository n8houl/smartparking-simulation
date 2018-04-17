import requests
import json
import random
import time

import sys

garage = sys.argv[1]

garages = ['A', 'B', 'C', 'D', 'H', 'I', 'Libra']
capacities = {'A': 1623, 'B': 1259, 'C': 1852, 'D': 1241, 'H': 1284, 'I': 1231, 'Libra': 1007, 'Test': 10}

url = 'http://18.218.108.116:3000/'
ret = requests.get(url + 'api/login/postable-user');

token_data = json.loads(ret.text)
token = token_data['token']

header = {'Authorization': 'Bearer %s' % token, 'Content-type': 'application/json'}

while(True):
	i = random.randrange(1, 3)
	time.sleep(i)

	if(garage == 'A'):
		i = random.randrange(1, capacities[garage])
	else:
		i = random.randrange(0, capacities[garage])
	spotId = '%04d' % i
	ret = requests.get(url + "spots/%s/%s" % (garage, spotId))
	js = json.loads(ret.text)
	occupied = js['occupied']

	requrl = '%sspots/%s/%s' % (url, garage, spotId)
	data = { "occupied" : (not occupied) }
	data_json = json.dumps(data)
	ret = requests.put(requrl, data=data_json, headers=header)
	print("sensor_%04d_garage%s:\n\tOccupied from %r to %r" % (i, garage, occupied, (not occupied)))
