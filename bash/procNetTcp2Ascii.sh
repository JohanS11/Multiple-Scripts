#!/bin/bash

#for port in $(cat openPorts | awk -F ":" '{print $2}' | sort -u); do echo "[+] Open Port: $(echo "obase=10; ibase=16; $port" | bc)"; done

if [ $1 ]; then

	for port in $(cat $1 | awk '{print $2}' | awk -F ":" '{print $2}' | sort -u); do
		echo "[+] Open Port : $(echo "obase=10; ibase=16; $port" | bc)"
	done
else
	echo -e "\nUsage : procNetTcp2Ascii <nettcpfile>"
fi
