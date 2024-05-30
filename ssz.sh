#! /usr/bin/bash

device=$(cat ~/bin/assets/devices.txt | fzf)
user=$(whoami)
ssh $user@$device
