#!/bin/bash

repos=$(curl https://api.github.com/users/psychoticpendulum/repos | jq | grep "\"name\":" | awk '{print $2}' | sort | uniq | sed s/\"//g | sed s/,//g)

for repo in $repos; do
	git clone https://$1@github.com/psychoticpendulum/$repo
done

