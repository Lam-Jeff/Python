#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import argparse
from base64 import b64encode


def generateKey (length) :
    return os.urandom (length)


def encrypt (message, key) :
    output = ""
    for i in range (len(message)) :
        current = message [i]
        current_key = key[i % len(key)]
        output += chr (ord (current) ^ ord (current_key))
    return output
def decrypt (message, key) :
    output = encrypt (message, key)
    return output



parser = argparse.ArgumentParser(description = "Encrypt or Decrypt using XOR cipher")
group = parser.add_mutually_exclusive_group()
group.add_argument ("-e", "--encrypt", action = "store_true", help = "encrypt the text")
group.add_argument ("-d", "--decrypt", action = "store_true", help = "decrypt the text")
parser.add_argument ("x", type = str, help = "the message encrypted or not")
parser.add_argument ("y", type = str, help = "the key",nargs = '?')

args = parser.parse_args()
if args.encrypt or args.decrypt :
    if args.y is None :
        KEY = generateKey (len (args.x))
    else :
        KEY = args.y
    MESSAGE = args.x

    print "Key : ",b64encode(KEY).decode ('utf8')
    print "Message : ",MESSAGE

if args.encrypt :
    print b64encode(encrypt (MESSAGE.encode('utf8'), KEY)).decode ('utf8')
elif args.decrypt :
    pass
else :
    print "You need an option, please refer to option --help"
