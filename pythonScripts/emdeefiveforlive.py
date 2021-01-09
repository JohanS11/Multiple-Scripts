#!/usr/bin/python3

import requests
import hashlib
import re

def getrequest(url,session):

    return session.get(url).text

def postrequest(url,data,session):

    out = session.post(url=url , data = data)
    return out.text

def striphtml(content):

    chars = re.search("<h3 align='center'>+.*?</h3>",content)
    chars = re.search("'>.*<",chars[0])
    chars = re.search("[^|'|>|<]...................",chars[0]) 
    return chars[0]

def main():
    
    requestsession = requests.session()
    url = "http://docker.hackthebox.eu:32216/"
    contentwithtags = getrequest(url,requestsession)
    content = striphtml(contentwithtags)
    md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
    data = {"hash" : md5}
    print(postrequest(url,data,requestsession))

if __name__ == '__main__':
    main()


