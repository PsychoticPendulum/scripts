#! /usr/bin/bash

if [[ -z "$(ip addr | grep tunr0)" ]]; then
	sudo wg-quick up tunr0
else
	sudo wg-quick down tunr0
fi
