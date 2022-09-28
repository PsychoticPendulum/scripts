#! /bin/bash

CMD=$(tac /home/$USER/.local/share/fish/fish_history | grep cmd | head -n 2 | tail -n 1)
NCMD=${CMD:7}
sudo $NCMD
