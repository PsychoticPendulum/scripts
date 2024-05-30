#! /usr/bin/bash

device=$(cat ~/bin/assets/devices.txt | fzf)
ssh luks@$device
