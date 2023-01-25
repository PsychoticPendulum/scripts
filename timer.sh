#! /usr/bin/bash

time=$1
if [[ -z $time ]]; then
	echo -n "Time (in s): "
	read time
fi

for i in $(eval echo "{1..$time}"); do
	echo "Sleeping [$i/$time]"
	sleep 1
	if [[ $i != $time ]]; then
		printf "\x1B[0m\x1B[1F\x1B[2K"
	fi
done

while true; do
	mpv ~/Developer/.scripts/assets/ringtone.mp4	
done
