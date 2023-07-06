#! /usr/bin/bash

if [[ -z $1 ]] || [[ -z $2 ]]; then
	echo "Not enough arguments given"
	exit
fi

lsblk | grep $1
if [[ $? -ne 0 ]]; then
	echo "Device not found"
	exit
fi

sudo cryptsetup luksOpen /dev/$1 $2
sudo mount /dev/mapper/$2 /mnt/media
