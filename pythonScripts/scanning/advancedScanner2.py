#!/usr/bin/env python

import optparse
from socket import *
from threading import *

def scanner(host,port):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        print("[+] Port %d/tcp Open!" % port)
    except:
        print("[-] Port %d/tcp Closed!" % port)
    finally:
        sock.close()
def portScan(host,ports):
    try:
        tgtIp = gethostbyname(host)
    except:
        print("Unknown host %s" % host)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("[+] Scans results for: " + tgtName[0])
    except:
        print("[+] Scans results for: "+ tgtIp)
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target = scanner, args=(host,int(port)))
        t.start()

    
        

def main():

    parser = optparse.OptionParser("Usage of this program: "+ "-H <target host> -p <target ports>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify the target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify the target port')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)


if __name__== '__main__':
    main()
    
