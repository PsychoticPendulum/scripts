#! /usr/bin/bash

cat ~/.config/i3/config | grep "bindsym" | sed s/"bindsym "//g
