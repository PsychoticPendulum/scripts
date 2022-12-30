#! /bin/bash
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

wrapper () {
	printf "\x1B[32;7m$1\x1B[0m\n"
}

clear

wrapper "Setting theme ..."
LAST=$(cat ~/Developer/.scripts/themes/.last.log)
sh ~/Developer/.scripts/theme.sh $LAST
feh --bg-scale ~/Wallpapers/wallpaper.jpg

wrapper "Cleaning up ..."
rm -Rfv ~/Downloads ~/Desktop
~/.screenlayout/focus.sh

wrapper "Setting keymap ..."
sudo sh ~/Developer/.scripts/keymod.sh

wrapper "Mounting shared partitions"
hostname=$(cat /etc/hostname)
if [[ $hostname == "tux" ]]; then
	sudo veracrypt /dev/nvme0n1p5 --keyfiles="/home/$USER/.keys/nvme0n1p5" ~/Files/School/
elif [[ $hostname -eq "psychosis" ]]; then
	sudo veracrypt /dev/sda --keyfiles="/home/$USER/.keys/sda" ~/Files/Downloads/
fi

wrapper "Creating tmux session"
tmux new-session -d -s music

wrapper "Starting Update Script ..."
sudo sh ~/Developer/.scripts/update.sh kek

wrapper "Updating repositories ..."
repull.sh

wrapper "Connecting to VPN ..."
python3 ~/Developer/.scripts/vpn.py

clear
bash
