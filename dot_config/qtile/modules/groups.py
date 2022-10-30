from libqtile.config import Group, Match, ScratchPad, DropDown
from .keys import terminal

# Group configuration
# 〇 
groups = [
    Group("Web", layout="monadtall", label=" ",
            matches = [Match(wm_class=["firefox"])]),
    Group("Files", layout="monadtall", label=" "),
    Group("Dev", layout="monadtall", label=" ",
            matches = [Match(wm_class=["Alacritty"])]),
    Group("Discord", layout="monadtall", label="ﭮ",
            matches = [Match(wm_class=["discord"])]),
    Group("System", layout="monadtall", label="  "),
]
