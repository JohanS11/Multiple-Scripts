#!/usr/bin/env python

import optparse
from threading import *
from socket import *

def scanner(host,port):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        print("[+] Port %d/tcp opened at %s host" %port %host)
    except:
        print("[-] Port %d/tcp closed at %s host" %port %host)
    finally:
        sock.close()

def portScan(host,ports):
    try:
        tgtIp = gethostbyname(host)
    except:
        print("Uknown host %s " % host)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("Scans results for: " + tgtName[0])
    except:
        print("Scans results for: " + tgtIp)
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=scanner, args=(host,int(port)))
        t.start()

def main():
    parser = optparse.OptionParser("Usage of this program: " + "-H <Target host> -p <Target ports>" )
    parser.add_option('-H',dest='tgtHost',type='string',help='Specify the target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='Specify the target ports separated by comma')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()
