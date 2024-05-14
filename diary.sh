#!/bin/bash

Info () {
    printf "\x1B[1;7m[Info]\x1B[0m\t$1\n"
}

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

local_file="$HOME/file/log/Diary.odt"
remote_file="/mnt/share/od/backup/file/log/Diary.odt"

if ! df | grep -q '/mnt/share/od'; then
	Info "Mounting OneDrive ..."
	rclone mount --daemon od: /mnt/share/od
	Status "Done"
fi

if [ $(stat -c %Y "$remote_file") -gt $(stat -c %Y "$local_file") ]; then
	Info "$remote_file is newer than $local_file"
	cp "$local_file" "$local_file.$(date +'%s').bak"
	Status "Creating backup of $local_file"
	cp "$remote_file" "$local_file"
	Status "Downloading $remote_file"
fi

Info "Opening diary ..."
libreoffice "$local_file"
Status "Diary saved"

Info "Copying diary to remote ..."
cp "$local_file" "$remote_file"
Status "Done"
