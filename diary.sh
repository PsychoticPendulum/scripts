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

if ! df | grep -q '/mnt/share/od'; then
	Info "Mounting OneDrive ..."
	rclone mount --daemon od: /mnt/share/od
	Status "Done"
fi

ramfs="$HOME/ramfs"

Info "Creating temporary filesystem ..."
mkdir ~/ramfs
sudo mount -t ramfs -o size=1G ramfs $ramfs
sudo chown -Rv $USER:$USER $ramfs

Info "Creating temporary password file ..."
echo -n "Decryption Cypher: "
read -s password
echo "OK"
echo $password > $ramfs/password

local_file="$HOME/ramfs/tmp.md"
remote_file="/mnt/share/od/log/diary.md.gpg"
password_file="$HOME/ramfs/password"

Info "Creating backup of remote file ..."
cp "$remote_file" "$remote_file.$(date +%Y-%m-%d)"
Info "Decrypting remote file ..."
gpg --decrypt --batch --passphrase-file $ramfs/password --output "$local_file" "$remote_file"
local_file_size=$(stat --format=%s "$local_file")
Info "Opening local copy ..."
vim "$local_file" -c 'set wrap nocursorcolumn colorcolumn=80'
Info "Encrypting local file ..."
gpg --symmetric --batch --passphrase-file $ramfs/password "$local_file"
Info "Moving local file back to remote ..."
cp -v "$local_file.gpg" "$remote_file"
Info "Removing temporary filesystem ..."
sudo umount ~/ramfs
rmdir ~/ramfs

tree -L 1 /mnt/share/od/log
