#! /usr/bin/bash

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

Info "Opening Diary ..."
libreoffice ~/.log/logbook/Diary.odt
Status "Saved Diary"

if ! df | grep -q '/mnt/share/OneDrive'; then 
	Info "Mounting OneDrive ..."
	rclone mount --daemon od: /mnt/share/OneDrive
	Status "Done"
fi

Info "Copying diary to OneDrive ..."
cp ~/.log/logbook/Diary.odt /mnt/share/OneDrive/
Status "Done"

if ! df | grep -q '/mnt/NAS'; then
	Info "Mounting NAS ..."
	sudo mount -t nfs 192.168.4.254:/nastier /mnt/NAS
	Status "Done"
fi

Info "Copying diary to NAS ..."
cp ~/.log/logbook/Diary.odt /mnt/NAS/backups/FullBackup/.log/logbook/
Status "Done"
