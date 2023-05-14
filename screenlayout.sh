#! /usr/bin/bash

if [[ $# -eq 0 ]]; then
	find /home/$USER/.screenlayout -type f -executable -exec basename {} \;
else
	/home/$USER/.screenlayout/"$1"
fi
