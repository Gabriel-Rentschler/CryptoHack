#!/bin/python3

from pwn import *;
from binascii import unhexlify;
from Crypto.Util.number import long_to_bytes, bytes_to_long;
import json;

import base64;
import codecs;

r = remote('socket.cryptohack.org', 13377, level = 'debug');
level = 0;

def json_recv():
    line = r.recvline();
    return json.loads(line.decode());

def json_send(hsh):
    request = json.dumps(hsh).encode();
    r.sendline(request);

def list_to_string(s):
    output = "";
    return(output.join(s));

while level <=100:
    received = json_recv();
    string = received["encoded"];
    encoding = received["type"];


    if encoding == "base64":
        string = base64.b64decode(string).decode('utf8').replace("'", '"');

    elif encoding == "hex":
        string = unhexlify(string).decode('utf8').replace("'", '"');

    elif encoding == "rot13":
        string = codecs.decode(string, 'rot_13');

    elif encoding == "bigint":
        string = unhexlify(string.replace("0x", "")).decode('utf8').replace("'", '"');

    elif encoding == "utf-8":
        string = list_to_string( [chr(b) for b in string] );

    to_send = {
            "decoded": string
    }
    json_send(to_send);

    level += 1;
