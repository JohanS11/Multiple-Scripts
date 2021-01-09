#!/usr/bin/python

from socket import *
from threading import *
import optparse

def scan(host,port):
    
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        print("El puerto %d/tcp esta abierto" %port)
    except:
        print("El puerto %d/tcp esta cerrado" %port)
    finally:
        sock.close()
        


def nameresolver(host,ports):
    try:
        tgtIp = gethostbyname(host)
    except:
        print("El host %s no ha sido identificado" %host)
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("[+] Resultados obtenidos para este host: " + tgtName[0])
    except:
        print("[+] Resultados obtenidos para este host: " + tgtIp)
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=scan, args=(host, int(port)))
        t.start()


def main():
    parser = optparse.OptionParser('Uso de este programa: ' + '-H <Host objetivo> -p <Puertos de objetivo>')
    parser.add_option('-H',dest='tgtHost',type='string',help="Por favor ingrese el host a escanear")
    parser.add_option('-p',dest='tgtPort',type='string',help="Por favor ingrese los puertos separados por coma")
    (options,args)= parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)  

    nameresolver(tgtHost,tgtPorts)
if __name__=='__main__':
    main()




