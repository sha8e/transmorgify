#!/usr/bin/env python
# Author: Michael Roberts
# Created: December 2015
# The following file relates to the tasks of creating, and interpreting hex data.

import binascii

BUFFSIZE = 1073741824


# Generates hex data from a file
def get_file_hex(file_data):

    try:
        with open(file_data, 'rb') as f:

            # maximum buffer size of 1GB in RAM
            buf = f.read(BUFFSIZE)
            gen_hex = ""

            # Until there is no more content keep reading data
            while len(buf) > 0:
                gen_hex += (binascii.hexlify(buf))
                buf = f.read(BUFFSIZE)

            return gen_hex

    except IOError:
        return '<!> The file "{}" does not exist'.format(file_data)


# Turns hex into a string
def hex_to_string(hex_data):
    # Remove any spaces in hex, if any
    hex_data = hex_data.replace(' ','')
    gen_string = binascii.unhexlify(hex_data)
    return gen_string


# Splits hex data (typeof bytes) into string, also splits into sections
def split_hex(hex_data, split_number=2):

    # Seeing if content has unnecessary characters
    if '\'' in str(hex_data):
        hex_data = str(hex_data).split("'")[1]
    else:
        hex_data = str(hex_data)

    new_string = str()
    split_every = split_number - 1
    count = 0

    # Splitting the string
    for c in hex_data:
        if count < split_every:
            count += 1
            new_string += c

        elif count == split_every:
            count = 0
            new_string += c + " "

    return new_string


# combination of getting a hex from file, and splitting it
def beautiful_hex(file_data, split_every=2):
    data = get_file_hex(file_data)

    if data:
        return split_hex(data, split_every)
    else:
        return False
