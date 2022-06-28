#! /bin/bash

ROOTDEV=$(lsblk | grep '/$' | awk '{print $1}')
ROOTDEV=${ROOTDEV:2}
hdparm -tT /dev/mapper/$ROOTDEV | tail -n 1 | awk '{print $11,$12}'
