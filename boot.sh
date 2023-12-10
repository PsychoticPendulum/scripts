#! /usr/bin/bash

Info () {
    printf "\x1B[1;7m[INFO]\x1B[0m\t$1\n"
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

Warning () {
    printf "\x1B[1;31m$1\x1B[0m\n"
}

Message () {
    printf "\x1B[1;35;7m$1\x1B[0m\n"
}


Status () {
	if [[ $? -eq 0 ]]; then
		Success "$1"
	else
		Fail "$2" "CONTINUE"
	fi
}

Info "Setting theme ..."
LAST=$(cat ~/bin/themes/.last.log)
bash ~/bin/theme.sh $LAST
~/.screenlayout/focus.sh
feh --bg-scale ~/file/pic/wallpapers/wallpaper.jpg
Status "Theme set!"

Info "Cleaning up ..."
rm -Rfv ~/Downloads ~/Desktop
sudo ~/bin/clean.py


Info "Setting keymap ..."
bash ~/bin/keymap.sh
setxkbmap us
Status "Keymap set!"

Info "Mounting shared partitions ..."
hostname=$(cat /etc/hostname)
if [[ $hostname == "tux" ]]; then
	sudo veracrypt /dev/nvme0n1p5 --keyfiles="/home/$USER/.keys/tux_nvme0n1p4" ~/Files/School/
elif [[ $hostname == "psychosis" ]]; then
	sudo veracrypt /dev/sda --keyfiles="/home/$USER/.keys/sda" ~/Files/Downloads/
fi
Status "Partitions mounted!"

Info "Creating tmux session ..."
tmux new-session -d -s music
Status "Created tmux session!"

Info "Starting Update Script ..."
upm --recheck update
Status "Updates installed!"

Info "Updating repositories ..."
~/bin/repull.sh
Status "Repositories are up to date!"

Info "Connecting to VPN ..."
python3 ~/bin/vpn.py
Status

clear
bash
