#!/usr/bin/env python3

f = open('ciphertext', 'r')
ciphertext = f.read()

for i in range(256):
    for c in ciphertext:
        print(chr((ord(c) + i) % 255), end="")
    print()

