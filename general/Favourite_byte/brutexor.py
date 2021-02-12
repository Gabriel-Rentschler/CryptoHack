#!/bin/python3

string = input("String to decode: ");

for keybyte in range(256):
    flag = "";

    final_str = bytes.fromhex(string).decode('ascii');

    for char in final_str:

        flag += chr(ord(char) ^ keybyte);

    if "crypto" in flag:
        print('This is the flag (probably): {}'.format(flag));
