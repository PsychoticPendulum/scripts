#! /bin/bash

set_theme () {
	cp ~/bin/themes/$1/i3.colorscheme ~/.config/i3/colorscheme
	cp ~/bin/themes/$1/i3.style ~/.config/i3/style
	cp ~/bin/themes/$1/polybar.colorscheme ~/.config/polybar/colorscheme
	cp ~/bin/themes/$1/polybar.style ~/.config/polybar/style
	cp ~/bin/themes/$1/kitty.conf ~/.config/kitty/kitty.conf
	cp ~/bin/themes/$1/wallpaper.jpg ~/Wallpapers/wallpaper.jpg
	feh --bg-fill ~/Wallpapers/wallpaper.jpg
	echo $1 > ~/Developer/.scripts/themes/.last.log
}

if [[ -z "$1" ]]; then
	theme=$(find ~/bin/themes/* -not -name '.*' -type d -exec basename {} \; | fzf)
	[[ -n $theme ]] && set_theme $theme
	killall polybar ; i3 restart ; clear
fi
