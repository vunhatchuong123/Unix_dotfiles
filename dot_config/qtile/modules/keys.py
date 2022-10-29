from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [

    # General commands
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Restart Qtile"),
    Key(
        [mod, "control", "shift"], "q",
        lazy.spawn("systemctl poweroff"),
        desc="Shutdown the computer",
    ),
    Key(
        [mod, "control", "shift"], "r",
        lazy.spawn("systemctl reboot"),
        desc="Restart the computer",
    ),

    # Change focus
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    #Key([mod], "Tab",
    #lazy.spawn("rofi -show window"),
    #desc="Rofi window switcher"),
    Key([mod, "shift"], "period",
        lazy.next_screen(),
        desc="Focus to next monitor"),

    # Change layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    # Move windows
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Resize windows
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "i",
        lazy.layout.grow(),
        desc="grow focused window at the expense of other columns"),
    Key([mod], "m",
        lazy.layout.shrink(),
        desc="shrink focused window while growing other columns"),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod], "o",
        lazy.layout.maximize(),
        desc="Makes focused window take maximum size"),
    Key([mod, "shift"], "space",
        lazy.layout.flip(),
        desc="Flips the main and secondary areas"),

    # Launch and close apps
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod], "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),
   # Key(
   #     [mod, "shift"],
   #     "Return",
   #     lazy.spawn("rofi -show drun"),
   #     desc="Launch Rofi in combined mode",
   # ),
    Key([mod], "Return",
        lazy.spawn("alacritty"),
        desc="Launch terminal"),
    Key([mod], "f",
        lazy.spawn("firefox"),
        desc="Chrome browser"),
    Key([mod], "v",
        lazy.spawn("code"),
        desc="VSCode"),
    Key([mod], "e",
        lazy.spawn("nautilus"),
        desc="Nautilus"),

    # Media keys
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle"),
        desc="Mute, unmute audio"),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next Track"),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"), desc="Previous Track"),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"), desc="Play/Pause Track"),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D default sset Master 2%+ unmute"),
        desc="Volume Up"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D default sset Master 2%- unmute"),
        desc="Volume Down"),

    # Scratch pad
    
    #Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('ranger')),

]
