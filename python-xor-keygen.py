#! /usr/bin/env python

xorkey = 'key'
string = 'ENTER ENCRYPTED STRING HERE'
password = ''

for _ in range(0, len(string), 1):
    password+=chr(ord(string[_]) ^ xorkey)

print(password)
