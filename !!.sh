#! /bin/bash

OUTPUT=$(tail -n 4 /home/$USER/.local/share/fish/fish_history | head -n 1)
OUTPUT=${OUTPUT:7}
sudo $OUTPUT
