#!/bin/python3

from binascii import unhexlify;
from pwn import *;

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313";
key2 = "";
key3 = "";
flag = "";

res1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e";
res2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1";
res3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf";

def xor_two_str(s1,s2):
    return ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(s1,s2));

key2 = xor_two_str(res1, key1);
print('key 2: {}'.format(key2));

key3 = xor_two_str(res2, key2);
print('key 3: {}'.format(key3));

final_key = xor_two_str(xor_two_str(key1, key2), key3);
print('Final key: {}'.format(final_key));

flag = xor_two_str(res3, final_key);
print('flag: {}'.format(flag));
