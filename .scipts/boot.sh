#! /bin/bash

echo "Setting Wallpaper ..."
feh --bg-scale ~/Wallpapers/ManjaroPlasmaPure.png
echo "Setting keymap to DE-LATIN1 ..."
sudo sh ~/Developer/.scripts/keymap.sh
echo "Starting Update Script ..."
sudo python3 ~/Developer/.scripts/update.py
echo "Connecting to VPN ..."
sudo python3 ~/Developer/.scripts/vpn.py
