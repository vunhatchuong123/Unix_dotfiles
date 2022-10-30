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
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),
#    Key([mod], "space",
#        lazy.layout.next(),
#        desc="Move window focus to other window"),
    #Key([mod], "Tab",
    #lazy.spawn("rofi -show window"),
    #desc="Rofi window switcher"),
    Key([mod], "period",
        lazy.next_screen(),
        desc="Focus to next monitor"),

    # Change layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),

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
#    Key([mod, "control"], "h",
#        lazy.layout.grow_left(),
#        desc="Grow window to the left"),
#    Key([mod, "control"], "l",
#        lazy.layout.grow_right(),
#        desc="Grow window to the right"),
#    Key([mod, "control"], "j",
#        lazy.layout.grow_down(),
#        desc="Grow window down"),
#    Key([mod, "control"], "k",
#        lazy.layout.grow_up(),
#        desc="Grow window up"),
    Key([mod], "h",
        lazy.layout.shrink(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.reset(),
        desc="Reset all window sizes"),
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
   
   #App Launcher
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
        lazy.spawn("media-notify mute"),
        desc="Mute, unmute audio"),
    Key([], "XF86AudioNext",
        lazy.spawn("media-notify next"),
        desc="Next Track"),
    Key([], "XF86AudioPrev",
        lazy.spawn("media-notify previous"), desc="Previous Track"),
    Key([], "XF86AudioPlay",
        lazy.spawn("media-notify play"), desc="Play/Pause Track"),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("media-notify up"),
        desc="Volume Up"),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("media-notify down"),
        desc="Volume Down"),
]

