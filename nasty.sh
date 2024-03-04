#! /usr/bin/bash

read -s -p "Password: " password

if [[ ! -z $password ]]; then 
	sudo mount -t cifs //192.168.4.1/nasty /mnt/nas -o username=luks,password=$password,uid=1000,gid=1000,file_mode=0664,dir_mode=0775
	tree -L 1 /mnt/NAS
fi

