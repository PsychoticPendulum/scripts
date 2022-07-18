#! /bin/bash

repull () {
 cd $1
 pwd
 git remote update
 git pull
 cd
}

repull ~/.config/
repull ~/Developer/.scripts/
