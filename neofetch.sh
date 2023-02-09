#! /usr/bin/bash

distro=$(lsb_release -d | awk '{print $2}')

if [[ $distro =~ "Void" ]]; then
	neofetch
elif [[ $distro =~ "Arch" ]]; then
	neofetch | lolcat -F 0.1 -a -s 5000 -S 174
else
	neofetch --config ~/.config/neofetch/config.conf.default
fi