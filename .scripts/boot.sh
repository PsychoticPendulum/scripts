#! /bin/bash
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

echo "Setting Wallpaper ..."
feh --bg-scale ~/Wallpapers/ArchPlasmaPure.png
echo "Setting keymap ..."
sudo sh ~/Developer/.scripts/keymap.sh
echo "Mounting secondary drive ..."
sudo mount /dev/sdb1 /mnt
echo "Starting Update Script ..."
sudo python3 ~/Developer/.scripts/update.py
echo "Connecting to VPN ..."
sudo python3 ~/Developer/.scripts/vpn.py
