#!/bin/bash

nitrogen --restore &
picom --config ~/.config/picom/picom.conf & disown

imwheel -b "4 5"

