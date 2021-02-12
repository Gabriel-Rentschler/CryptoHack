#!/bin/python3

def xor_two_str(s1,s2):
    return ''.join(format(int(a, 16) ^ int(ord(b)), 'x') for a,b in zip(s1,s2));


string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104";
key = "XOR";

print(xor_two_str(string, key));
