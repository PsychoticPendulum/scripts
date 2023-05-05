#! /usr/bin/bash

if [[ ! -f /usr/bin/tree ]]; then
    echo "Tree is not installed."
    exit 1
fi

if [[ -z $(df -h | grep 'nasty') ]]; then
    echo "nasty is not mounted"
    exit 1
fi

echo "Indexing Music ..."
tree -L 2 /mnt/NAS/Music > ~/.info/Music.txt
echo "Indexing Series ..."
tree -L 2 /mnt/NAS/Series > ~/.info/Series.txt
echo "Indexing Movies ..."
tree -L 1 /mnt/NAS/Movies > ~/.info/Movies.txt