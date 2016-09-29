#!/bin/bash

ps -ef | grep -v "grep" | grep "ffmpeg\|node\|start_"
