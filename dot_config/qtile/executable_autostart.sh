#!/bin/bash

nitrogen --restore &
picom --config ~/.config/picom/picom.conf & disown
xrandr --output DP-4 --primary --mode 2560x1440 --rate 74.92
xrandr --output HDMI-0 --mode 1920x1080 --right-of DP-4

pasystray &

