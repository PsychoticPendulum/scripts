# Startup Script
xmodmap -e 'keycode 66 = Escape'
xmodmap -e 'clear lock'

# User Aliases for FISH
echo "Setting Aliases ..."

# Scripts
alias please="sudo"
alias nvpn="sudo python3 ~/Developer/.scripts/vpn.py"
alias loaf="python3 ~/Developer/.scripts/loaf.py"
alias cls="cd && clear && bash"
alias bonsai="python3 ~/Developer/.scripts/bonsai.py"

# Lolcat
alias rangerl="ranger | lolcat"
alias htopl="htop | lolcat"
alias cmatrixl="cmatrix | lolcat"
alias cat="lolcat"

# ptsh
alias lsa="ptls -a"
alias touch="pttouch"
alias mkdir="ptmkdir"

# Network
alias snf="sudo python3 ~/Developer/PizzaGate/packetsniffer.py"

# Games
alias gol="python3 ~/Developer/PYTHON/GameOfLife2/GameOfLife.py"
alias fb="python3 ~/Developer/PYTHON/FlappyBlock/FlappyBlock.py"
alias rr="python3 ~/Developer/PYTHON/RunningRonnie/RunningRonnie.py"
alias pong="python3 ~/Developer/PYTHON/Pong/Pong.py"
