#!/usr/bin/env python3

from socket import *
from threading import *
import sys, queue

openports = []

def portScan(host,ports):
    global openports
    try:
        tgtIp = gethostbyname(host)
    except:
        print("Host %s has not been resolved" %host)
        exit(0)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("[+] Scan results for: " + tgtName[0])
    except:
        print("[x] Couldn't connect to host ") + tgtIp
        exit(0)
    setdefaulttimeout(1)

    for port in ports:
        t = Thread(target=scanner, args=(host,int(port)))
        t.start()

def scanner(host,port):

    global openports

    sock = socket(AF_INET,SOCK_STREAM)
    if (sock.connect_ex((host,port))):
        pass
    else:
        
        openports.append(port)
        ports = ','.join(map(str, openports)) 
        print("[+] Open ports " , ports)
        


def usage():
    banner = """
    ____          __   __                     _____                                       
   / __ \ __  __ / /_ / /_   ____   ____     / ___/ _____ ____ _ ____   ____   ___   _____
  / /_/ // / / // __// __ \ / __ \ / __ \    \__ \ / ___// __ `// __ \ / __ \ / _ \ / ___/
 / ____// /_/ // /_ / / / // /_/ // / / /   ___/ // /__ / /_/ // / / // / / //  __// /    
/_/     \__, / \__//_/ /_/ \____//_/ /_/   /____/ \___/ \__,_//_/ /_//_/ /_/ \___//_/     
       /____/"""
    
    banner+= "\nUsage: advancedScanner.py -h (print this banner) -H <host> -p <port list separated by comma> or -a (All ports)"

    return banner

def main():
    global portsopen
    try :
        if (sys.argv[1] == None) : print("?")
    except :   
        print(usage())
        exit(0)
    if (sys.argv[1] == '-h' or sys.argv[1] !="-H" ):
        print(usage())
        exit(0)

    tgtHost = str(sys.argv[2])

    if (sys.argv[3] == '-p'):
        tgtPorts = str(sys.argv[4]).split(',')
    elif (sys.argv[3] == '-a'):
        tgtPorts = [str(i) for i in range(65535)]
    else : 
        print(usage()) 
        exit(0)
        
    portScan(tgtHost,tgtPorts)
   
    
if __name__ == '__main__':
    main()
