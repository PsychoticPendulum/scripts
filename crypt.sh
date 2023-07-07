#! /usr/bin/bash

Success () {
    printf "\x1B[1;32;7m[ OK ]\x1B[0m\t$1\n"
}

Fail () {
    printf "\x1B[1;31;7m[FAIL]\x1B[0m\t$1\n"
	if [[ -z $2 ]]; then
		exit 1
	fi
}

Status () {
	if [[ $? -eq 0 ]]; then
		Success "$1"
	else
		Fail "$2" "CONTINUE"
	fi
}

action=$(printf "mount\numount" | fzf)

if [[ $action == "mount" ]]; then
	lsblk
	read -p "Enter device: " device
	
	if ! lsblk | grep -q $device; then
		Fail "Device not found"
		exit
	fi

	name=$(cat /dev/urandom | tr -dc 'a-f0-9' | head -c 4)
	mountpoint=$(ls /mnt | fzf)

	sudo cryptsetup luksOpen /dev/$device luks-$name
	Status "Opening device $device"
	sudo mount /dev/mapper/luks-$name /mnt/$mountpoint
	Status "Mounting $device at $mountpoint"

	read -p "Do you want to cd to $mountpoint? [Y/n] " answer
	if [[ $answer = "N" ]] || [[ $answer == "n" ]]; then
		exit
	fi

	clear
	Success "Changing directory to $mountpoint"
	cd /mnt/$mountpoint
	ranger

elif [[ $action == "umount" ]]; then
	mountpoint=$(lsblk -no MOUNTPOINT | grep "/" | fzf)
	device=$(lsblk | grep $mountpoint | grep -o -E 'luks-[0-9a-f]{4}')

	if [[ -z $device ]]; then
		Fail "Device not found for: $mountpoint"
		exit
	fi
	
	sudo umount $mountpoint
	Status "Unmounting $mountpoint"
	sudo cryptsetup luksClose /dev/mapper/$device
	Status "Closing device $device"
fi
