#!/usr/bin/env python3

import json

f = open('incidents.json', 'r')
parsed_json = json.loads(f.read())

# Problems 1 and 2: Get the source IP address that appears the most and the number of unique destination IP addresses
src_ip_hash = {}
unique_dest_ip = {}

for fields in parsed_json["tickets"]:
	src_ip = fields['src_ip']
	dst_ip = fields['dst_ip']
	if src_ip not in src_ip_hash:
		src_ip_hash[src_ip] = 1
	else:
		src_ip_hash[src_ip] += 1
	if dst_ip not in unique_dest_ip:
		unique_dest_ip[dst_ip] = 1

print(max(src_ip_hash, key=src_ip_hash.get))
print(len(unique_dest_ip))


# Problem 3: Get average number of destination addresses sent
hashes = {}
for each in parsed_json["tickets"]:
	h = each["file_hash"]
	if h not in hashes:
		hashes[h] = set()
	hashes[h].add(each['dst_ip'])

avg = 0
for each in hashes:
	ip = hashes[each]
	avg += len(ip)
avg = (avg * 1.0) / len(hashes)

print(avg)
