#! /bin/bash

IP=$(curl -s ipinfo.io | head -n 2 | tail -n 1)
IP=${IP:9}
IP=${IP::-2}
echo $IP | cowsay -f tux
