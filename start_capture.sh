#!/bin/bash

sudo modprobe bcm2835-v4l2 && ffmpeg -s 640x320 -f video4linux2 -i /dev/video0 -f mpeg1video -b 800k -r 30 http://127.0.0.1:8082/raspberry/640/320
