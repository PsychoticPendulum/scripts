#! /bin/bash
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

distro=$(lsb_release -d | awk '{print $2 $3}')
echo -n "Do you want to check for updates? [Y/n] "
read answer

if [[ $answer == Y ]] || [[ -z $answer ]]; then
	if [[ $distro =~ "Void" ]]; then
		printf "Detected Operating System: \x1B[1;35m$distro\x1B[0m\n"
		sudo xbps-install -Syu
	elif [[ $distro =~ "Arch" ]]; then
		printf "Detected Operating System: \x1B[1;36m$distro\x1B[0m\n"
		yay -Syu
	else
		printf "Detected Operating System: \x1B[1m$distro\x1B[0m\n"
		sudo apt update && sudo apt upgrade
	fi
fi
