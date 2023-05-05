#! /usr/bin/bash

WALLPAPER=$(ls ~/Wallpapers/*.* | shuf | head -n 1)
feh --bg-fill $WALLPAPER
