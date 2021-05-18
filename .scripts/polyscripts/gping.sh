ping -qc1 google.com 2>&1 | awk -F'/' 'END{ print (/^rtt/? "Google.com: "$5" ms":"Google.com: DOWN") }'
