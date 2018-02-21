#!/usr/bin/python
# Amazon dash button intercept with hooks to home-assistant
# Can be extended to other services
# Written by Roger Rainey roger.rain@gmail.com
# 2/20/2018

import requests, json, time, yaml, os

from scapy.all import sniff
from scapy.all import ARP

file = open('config/buttons.yaml','r')
byaml = yaml.load(file)
file.close()

macList = [] # Gather a list of Dash buttons

for button in byaml['buttons']:
	macList.append(button['mac'])

lastTime = 0 # Keep from running too often
def button_action(index):
	global lastTime
	useButton = byaml['buttons'][index] # The button pressed
	if (time.time() - lastTime) > 10:
		for service in useButton['service']:
			# Check to see if this is for home assistant
			# other actions can be scripted here
			if service['service_type'] == 'home-assistant':
				headers = { service['http_headers']['http_header'] : service['http_headers']['http_header_value'],
							'Content-Type' : service['content_type'] }
				payload = { 'entity_id' : service['payload']['entity_id'] }
				req = requests.post(service['payload']['url'], data=json.dumps(payload), headers=headers)
		lastTime = time.time()

def arp_display(pkt):
	if pkt[ARP].op == 1:
		if pkt[ARP].hwsrc in macList:
			index = macList.index(pkt[ARP].hwsrc)
			button_action(index)

print(sniff(prn=arp_display, filter="arp", store=0))