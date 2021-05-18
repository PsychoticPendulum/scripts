#!usr/bin/env bash

killall -q polybar
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar bar1 >> /tmp/polybar1.log 2>&1 &
polybar bar2 >> /tmp/polybar2.log 2>&1 &

echo "Bars launched ..."
