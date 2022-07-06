#! /bin/bash

CURRENT=$(setxkbmap -query | tail -n 1 | awk '{print $2}')

echo Current is $CURRENT

if [[ $CURRENT == "de" ]]; then
	echo 'Setting to en_US'
	setxkbmap en_US
else
	echo 'Setting to de'
	setxkbmap de
fi
