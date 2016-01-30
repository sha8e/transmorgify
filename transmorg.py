#!/usr/bin/env python
# Author: Michael Roberts
# Created: January 2016
# This file converts any file into a jpg. It can be edited for different file types.

import hex_util
import os
import binascii

prompt = ">"
magic_number = "4A464946"
change_file = raw_input("> File to hex: ")

file_hex = hex_util.get_file_hex(change_file)
print("{} {}'s hex is:\n{}").format(prompt,change_file,file_hex)

print ("{} Converting to JPG...").format(prompt)
new_hex = magic_number + file_hex

with open(change_file, 'wb') as f:
    f.write(binascii.unhexlify(new_hex))

first_part = change_file.split('.')[0]
os.rename(change_file,first_part + '.jpg')
new_file_hex = hex_util.get_file_hex(first_part + '.jpg')
print("{} {}'s hex is now:\n{}").format(prompt,change_file,new_file_hex)
