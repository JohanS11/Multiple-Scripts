#!/usr/bin/python

from socket import *
from termcolor import colored

def scan(host,port):
    sock = socket(AF_INET,SOCK_STREAM)

    if (sock.connect_ex((host,port))):
        print(colored("[x] The port %d is closed" %(port),'red'))
    else:
        print(colored("[+] The port %d is open" %(port),'green'))

def main():
    for i in range(446):
        scan("127.0.0.1",i)

if __name__ == '__main__':
    main()
