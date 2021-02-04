#!/bin/bash

for i in {1..255}
do
	ping -c1 192.168.57.$i > /dev/null
	rta=$?
	if [ $rta -eq 0 ] 
	then
		echo host $i activo
	fi
done 
		
