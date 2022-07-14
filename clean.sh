#! /bin/bash

BEFORE=$(df / | awk '{print $3}' | tail -n 1)

paccache -r
rm -Rfv ~/.cache/yay/*
rm -Rfv ~/.cache/vim/*/*

AFTER=$(df / | awk '{print $3}' | tail -n 1)

TOTAL=$(($BEFORE - $AFTER))

echo cleaned up $TOTAL bytes
