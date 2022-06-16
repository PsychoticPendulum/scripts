#! /bin/bash

if [[ -z "$1" ]]; then
	echo "Usage: asm <file>"
	exit
fi

filename=$1
file=${filename::-4}

nasm -felf64 $file.asm -o $file.o && ld $file.o -o $file && ./$file
