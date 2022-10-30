import os
from libqtile import bar
from .widgets import *
from libqtile.config import Screen

wallpaper_path = os.path.expanduser("~") + "/.local/share/backgrounds/"

# Screen and bar configuration
screens = [
    Screen(
        top=bar.Bar(
            widgets=init_bar_widgets(),
            size=30,
            margin=[5, 5, 0, 5],
            background  = colors["base"]
        ),

#        wallpaper=wallpaper_path + "beyond_the_clouds_v01.png",
#        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets=init_bar_widgets(primary=False),
            size=30,
            margin=[5, 5, 0, 5],
        background  = colors["base"]
        ),
#        wallpaper=wallpaper_path + "beyond_the_clouds_v01.png",
#        wallpaper_mode="fill"
    ),
]
