#!/bin/bash

# Function to list tmux sessions and format for dialog
list_sessions() {
    tmux list-sessions -F '#S' 2>/dev/null
}

# Function to prompt for a new session name
prompt_for_session_name() {
    # Use dialog to ask for the session name
    session_name=$(dialog --title "New Session Name" --inputbox "Enter the name for the new session:" 8 40 3>&1 1>&2 2>&3)
    echo "$session_name"
}

# Function to create a dialog menu from tmux sessions, with an option to create a new session
choose_session() {
    # Store the session list in an array
    mapfile -t sessions < <(list_sessions)

    if [ ${#sessions[@]} -eq 0 ]; then
        # Automatically create a new session if none exists
        session_name=$(prompt_for_session_name)
        if [ -z "$session_name" ]; then
            session_name="default"  # Default name if none provided
        fi
        tmux new-session -s "$session_name" -d
        tmux attach-session -t "$session_name"
        exit
    fi

    # Create menu options
    local options=()
    local index=0
    for session in "${sessions[@]}"; do
        options+=("$index" "$session")
        ((index++))
    done

    # Add an option to create a new session
    options+=("$index" "Create New Session")

    # Show dialog menu to select a session or create a new one
    choice=$(dialog --title "Select or Create tmux Session" --menu "Choose a session or create a new one:" 15 60 6 "${options[@]}" 3>&1 1>&2 2>&3)

    # Process user's selection
    if [ "$?" -eq 0 ]; then
        if [ "$choice" -eq "$index" ]; then
            # User chose to create a new session
            session_name=$(prompt_for_session_name)
            if [ -z "$session_name" ]; then
                session_name="new_session"  # Default name if none provided
            fi
            tmux new-session -s "$session_name" -d
            tmux attach-session -t "$session_name"
        else
            # User selected an existing session
            tmux attach-session -t "${sessions[$choice]}"
        fi
    else
        # User cancelled or closed the dialog; exit or handle accordingly
        echo "No session selected. Exiting..."
        exit
    fi
}

# Run the function to choose a session
choose_session

