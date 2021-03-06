#!/bin/bash
for share in $(find . -type d) 
do
    sudo /usr/bin/touch $share/test 2>/dev/null
    cmd_state=$?
    if [ $cmd_state -eq 0 ]
      then /usr/bin/echo $share writable
    fi
done
