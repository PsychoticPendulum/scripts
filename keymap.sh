#! /bin/bash

CURRENT=$(setxkbmap -query | grep "layout" | awk '{print $2}')

echo Current is $CURRENT

if [[ $CURRENT == "de" ]]; then
	echo 'Setting to us'
	setxkbmap us 
else
	echo 'Setting to de'
	setxkbmap de
fi

~/Developer/.scripts/keymod.sh
