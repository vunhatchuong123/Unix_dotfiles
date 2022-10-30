#!/bin/bash

nitrogen --restore &
picom --config ~/.config/picom/picom.conf & disown
dunst -conf ~/.config/dunst/catppuccinrc &

imwheel -b "4 5"
