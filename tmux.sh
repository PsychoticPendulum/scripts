#! /usr/bin/bash

session_name=$(tmux list-sessions -F '#S' | fzf)

if [ -n "$session_name" ]; then
    tmux attach-session -t "$session_name"
fi

