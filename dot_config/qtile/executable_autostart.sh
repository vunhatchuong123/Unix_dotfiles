#!/bin/bash

# Wallpaper
nitrogen --restore &

# Composer
picom --config ~/.config/picom/picom.conf & disown

# Notifier
dunst -conf ~/.config/dunst/catppuccinrc &

# Volume control
pasystray &

# Network Manager
nm-applet &

# Mouse Wheel
imwheel -b "4 5"

# xfce4-power-manager &
