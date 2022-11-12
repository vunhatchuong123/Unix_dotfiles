#!/bin/env bash

# Options for powermenu
lock="    Lock"
logout="    Logout"
shutdown="    Shutdown"
reboot="    Reboot"
sleep="    Sleep"

# Get answer from user via rofi
selected_option=$(echo "$lock
$logout
$sleep
$reboot
$shutdown" | rofi -dmenu\
                  -i\
                  -p "Power"\
                  -theme-str 'configuration{
                  font: "JetBrainsMono Nerd Font 12";}
                              window{
                              border: 0;
                              width: 250px;
                              padding: 10;
                              transparency: "real";}
                              '\
                  )

# Do something based on selected option
if [ "$selected_option" == "$lock" ]
then
    loginctl lock-session ${XDG_SESSION_ID-}
elif [ "$selected_option" == "$logout" ]
then
    loginctl terminate-user `whoami`
elif [ "$selected_option" == "$shutdown" ]
then
    systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
    systemctl reboot
elif [ "$selected_option" == "$sleep" ]
then
    amixer set Master mute
    systemctl suspend
else
    echo "No match"
fi


