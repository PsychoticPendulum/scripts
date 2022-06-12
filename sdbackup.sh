#! /bin/bash
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

MATE="psychicpenguin"

echo -n "Do you want to create a backup of the SD Card? [Y/n] "
read answer

header () {
	sep -b 5
	figlet $1
}

if [[ "$answer" == "Y" ]]; then
	header "Log"
	sudo cp -Rfv /home/$MATE/.log/logbook/Diary.odt /mnt/veracrypt1/Backups/Linux/.log/logbook/Diary.odt
	header "School"
	sudo rsync -rv /mnt/veracrypt1/School /home/$MATE/.school
	sudo chown -R $USER:$USER /home/$MATE/.school/
	header "Developer"
	sudo rsync -rv /home/$MATE/Developer/* /mnt/veracrypt1/Code/
fi
