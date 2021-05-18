ping -qc1 fuckinl.it 2>&1 | awk -F'/' 'END{ print (/^rtt/? "fuckinl.it: "$5" ms":"fuckinl.it: DOWN") }'
