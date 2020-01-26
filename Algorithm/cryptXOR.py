#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import argparse
from base64 import b64encode
from base64 import b64decode


def generateKey (length) :
    return os.urandom (length)


def encrypt_decrypt (message, key) :
    output = ""
    for i in range (len(message)) :
        current = message [i]
        current_key = key[i % len(key)]
        output += chr (ord (current) ^ ord (current_key))
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

    print "Key : ",b64encode(KEY)
    print "Message : ",MESSAGE

if args.encrypt :
    print "Encoding..."
    print b64encode(encrypt_decrypt (MESSAGE.encode ('utf8'), KEY))
elif args.decrypt :
    print "Decoding..."
    print b64decode (b64encode (encrypt_decrypt (MESSAGE, KEY) + "===")).decode ('utf8')
else :
    print "You need an option, please refer to option --help"
