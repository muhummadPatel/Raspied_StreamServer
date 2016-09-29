#!/bin/bash

echo 'Starting streaming server as bg process...'
2>/dev/null 1>/dev/null /home/pi/start_server.sh &

sleep 10

echo 'Starting video capture as bg process...'
2>/dev/null 1>/dev/null /home/pi/start_capture.sh > /dev/null &
