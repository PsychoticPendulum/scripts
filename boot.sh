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
	sep -b 4 -l 1
}

clear

~/.screenlayout/focus.sh

wrapper "Launching Polybar ..."
killall polybar
sh ~/.config/polybar/launch.sh &
i3 restart

wrapper "Setting theme ..."
LAST=$(cat ~/Developer/.scripts/themes/.last.log)
sh ~/Developer/.scripts/theme.sh $LAST
feh --bg-scale ~/Wallpapers/wallpaper.jpg

wrapper "Setting keymap ..."
sudo sh ~/Developer/.scripts/keymod.sh

# wrapper "Mounting MicroSD ..."
# sudo veracrypt /dev/mmcblk0p1 && sudo sh ~/Developer/.scripts/sdbackup.sh 
# sudo mount /dev/mmcblk0p1 /mnt/SD

wrapper "Starting Update Script ..."
sudo sh ~/Developer/.scripts/update.sh kek ; repull.sh

wrapper "Connecting to VPN ..."
sudo python3 ~/Developer/.scripts/vpn.py
clear
bash
