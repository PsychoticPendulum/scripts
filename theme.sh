#! /bin/bash

exit

set_theme () {
	cp ~/Developer/.scripts/themes/$1/i3.config ~/.config/i3/config
	cp ~/Developer/.scripts/themes/$1/polybar.config ~/.config/polybar/config
	cp ~/Developer/.scripts/themes/$1/xfce4_terminal.config ~/.config/xfce4/terminal/terminalrc
	cp ~/Developer/.scripts/themes/$1/kitty.config ~/.config/kitty/kitty.conf
	cp ~/Developer/.scripts/themes/$1/wallpaper.jpg ~/Wallpapers/wallpaper.jpg
	feh --bg-fill ~/Wallpapers/wallpaper.jpg
	echo $1 > ~/Developer/.scripts/themes/.last.log
}

if [[ -z "$1" ]]; then
	echo "Usage: 	theme [option]."
	echo "Available Themes:"
	ls ~/Developer/.scripts/themes/
	exit
else
	set_theme $1
fi

killall polybar
i3 restart
clear
