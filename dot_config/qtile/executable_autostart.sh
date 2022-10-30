#!/bin/bash

nitrogen --restore &
picom --config ~/.config/picom/picom.conf & disown
dunst -conf ~/.config/dunst/qtilerc &

imwheel -b "4 5"
