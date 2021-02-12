#!/bin/python3

string= "label";
key = 13;
flag = "";

for char in string:
    flag += chr(ord(char) ^ key)

print(flag);
