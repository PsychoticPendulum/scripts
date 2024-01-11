#! /usr/bin/bash

SESSION=$(ls ~/.local/share/remmina/ | rofi -dmenu window -lines 0 -eh 1 -location 0 -width 644 -font "Source Code Pro Medium 10" -theme "~/.config/rofi/spotlight.rasi")
if ! [ -z $SESSION ]; then
	remmina --connect=$HOME/.local/share/remmina/$SESSION
fi
