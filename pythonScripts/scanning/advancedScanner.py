#!/usr/bin/python

from socket import *
from threading import *
import optparse

def portScan(host,ports):
    try:
        tgtIp = gethostbyname(host)
    except:
        print("Host %s has not been resolved" %host)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("[+] Scan results for: " + tgtName[0])
    except:
        print("[+] Scan results for: ") + tgtIp
    setdefaulttimeout(1)
    for port in ports:
       t = Thread(target=scanner, args=(host,int(port)))
       t.start()


def scanner(host,port):
    sock = socket(AF_INET,SOCK_STREAM)
    if (sock.connect_ex((host,port))):
        print("[-] %d/tcp Closed" % port)
    else:
        print("[+] %d/tcp Open" % port)

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <Target host> -p <Target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()
