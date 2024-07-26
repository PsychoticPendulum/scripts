#! /usr/bin/bash

hostnames=$(jq -r 'keys[]' ~/bin/assets/devices.json)

selected_hostname=$(echo "$hostnames" | fzf --prompt="Select a hostname: ")

if [ -n "$selected_hostname" ]; then
    ip_address=$(jq -r --arg host "$selected_hostname" '.[$host]' ~/bin/assets/devices.json)
    ssh $USER@$ip_address
else
    echo "No hostname selected"
fi

