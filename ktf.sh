#! /usr/bin/fish

set cmd $(history | grep -E "^k" | sort | uniq | fzf)
echo $cmd | bat --language fish
commandline $cmd
