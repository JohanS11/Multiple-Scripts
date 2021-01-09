#!/usr/bin/python

import hashlib

sha1hash = input("Enter sha1 hash value: ")
wordlist= open('/usr/share/wordlists/rockyou.txt','r',encoding="ascii", errors="surrogateescape")
passwordlist = wordlist.read()
print(passwordlist[0])
for password in passwordlist.split('\n'):
    hashguess= hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash :
        print("[+] The password is: "+ str(password))
        quit()
    else:
        print("[-] Password guess" + str(password)+ " does not match, trying next...")
print("Password not in passwordlist")
