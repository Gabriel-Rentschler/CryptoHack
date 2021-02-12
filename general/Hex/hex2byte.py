#!/bin/python3

from binascii import unhexlify;
import base64;

string = input('Hex string: ');

string = bytes.fromhex(string).decode('ascii');
print(string);
