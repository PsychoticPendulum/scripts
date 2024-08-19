#!/bin/bash

session_name=$(tmux list-sessions -F '#S' | fzf --height=20% --reverse)

if [ -n "$session_name" ]; then
    tmux attach-session -t "$session_name"
else
    echo "No session selected."
fi

