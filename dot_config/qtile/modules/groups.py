from libqtile.config import Group, Match
from .keys import keys, mod

# Group configuration
groups = [
    Group("Web", layout="monadtall", label=" "
            matches = [Match(wm_class=["Firefox"])]),
    Group("Files", layout="monadtall", label=""),
    Group("Dev", layout="monadtall", label="",
            matches = [Match(wm_class=["Alacritty"])]),
    Group("Discord", layout="monadtall", label="ﭮ",
            matches = [Match(wm_class=["discord"])]),
    Group("System", layout="monadtall", label=""),
]
