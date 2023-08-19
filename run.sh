#!/bin/bash

set -o allexport
source /home/pi/.keys/w2g.env
set +o allexport

python3 /home/pi/git/discord-w2g/bot.py
