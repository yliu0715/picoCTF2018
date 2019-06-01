#!/usr/bin/env python3

import pwn
import re
import codecs

sh = pwn.remote('2018shell.picoctf.com', 31711)

# Convert from base 2 to ASCII
prompt_1 = str(sh.recv())
print(prompt_1)
binary = ''.join(re.findall('(\d{8}\s*)', prompt_1)).replace(" ", "")
word = codecs.decode(hex(int(binary,2))[2:], 'hex').decode('utf-8')
sh.sendline(word)

# Convert from base 16 to ASCII
prompt_2 = str(sh.recv())
print(prompt_2)
hexa = re.findall('[0-9a-f]+', prompt_2)[6]
sh.sendline(codecs.decode(hexa, 'hex').decode('utf-8'))

# Convert from base 8 to ASCII
prompt_3 = str(sh.recv())
print(prompt_3)
octa = re.findall('([0-7]{3})+', prompt_3)
word_list = [codecs.decode(hex(int(i,8))[2:], 'hex').decode('utf-8') for i in octa]
sh.sendline(''.join(word_list).replace(" ", ""))

# Get flag
prompt_4 = str(sh.recv())
print(prompt_4)
flag = ''.join(re.findall('picoCTF{.*}', prompt_4))
print(flag)

sh.close()
