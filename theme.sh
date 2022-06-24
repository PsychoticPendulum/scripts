#! /bin/bash

set_theme () {
	cp ~/Developer/.scripts/themes/$1/i3.colorscheme ~/.config/i3/colorscheme
	cp ~/Developer/.scripts/themes/$1/i3.style ~/.config/i3/style
	cp ~/Developer/.scripts/themes/$1/polybar.colorscheme ~/.config/polybar/colorscheme
	cp ~/Developer/.scripts/themes/$1/polybar.style ~/.config/polybar/style
	cp ~/Developer/.scripts/themes/$1/kitty.conf ~/.config/kitty/kitty.conf
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
