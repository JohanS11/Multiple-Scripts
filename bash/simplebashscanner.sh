
for port in $(seq $2 $3); 
  do
    timeout 1 bash -c "echo "" > /dev/tcp/$1/$port" &>/dev/null
    if [ $? -eq 0 ]; 
      then echo "[+] $port open" 
    fi
  done
