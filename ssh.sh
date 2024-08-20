#!/bin/bash

# Define the JSON file
json_file="$HOME/bin/assets/hosts.json"

# Extract hostnames and IPs from the JSON file
mapfile -t hosts < <(jq -r 'keys[]' "$json_file")
mapfile -t ips < <(jq -r '.[].hostname' "$json_file")

# Select a hostname using fzf
selected_hostname=$(printf "%s\n" "${hosts[@]}" | fzf --prompt="Select a hostname: ")

# Find the corresponding IP
selected_ip=$(jq -r --arg hostname "$selected_hostname" '.[$hostname]' "$json_file")

# Connect to the selected hostname
if [ -n "$selected_ip" ]; then
    ssh "$USER@$selected_ip"
else
    echo "No IP found for the selected hostname."
fi

