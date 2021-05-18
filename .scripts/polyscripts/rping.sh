ping -qc1 reddit.com 2>&1 | awk -F'/' 'END{ print (/^rtt/? "reddit.com: "$5" ms":"reddit.com: DOWN") }'
