#!/usr/bin/env python 

from socket import *
from sys import *
from termcolor import colored

def scan(host,port):
    sock = socket(AF_INET,SOCK_STREAM)
    
    if (sock.connect_ex((host,port))):
        print(colored("[-] The port %d is closed" % port ,'red'))
    else:
        print(colored("[+] The port %d is open"  % port,'green'))
def main():
    
    for port in range(446):

        scan(argv[1],port)

if __name__== '__main__':
    main()

        

