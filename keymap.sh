#! /bin/bash

CURRENT=$(setxkbmap -query | tail -n 1 | awk '{print $2}')

echo Current is $CURRENT

if [[ $CURRENT == "de" ]]; then
	echo 'Setting to us'
	setxkbmap us 
else
	echo 'Setting to de'
	setxkbmap de
fi
xmodmap /etc/xmodmap.conf

echo "Settings keyrate to 300, 50 ..."
xset r rate 300 50
