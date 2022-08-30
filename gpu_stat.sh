#! /bin/bash

GPU=$(radeontop --limit 1 --dump - | tail -n 1 | awk '{print $4$5$26$27}' | sed s/'gpu'/'GPU: '/g | sed s/'vram'/'vRam: '/g | sed s/','/' '/g)
GPU=${GPU::-1}
echo $GPU
