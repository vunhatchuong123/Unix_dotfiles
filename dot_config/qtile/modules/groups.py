from libqtile.config import Group, Match, ScratchPad, DropDown
from .keys import terminal

# Group configuration
# 〇 
groups = [
    Group("Web", layout="monadtall", label=" ",
            matches = [Match(wm_class=["firefox"])]),
    Group("Dev", layout="monadtall", label=" ",
            matches = [Match(wm_class=["Alacritty"])],
            screen_affinity = 2,
          ),
    Group("Code", layout="monadtall", label=" ",
            matches = [Match(wm_class=["code"])]),
    Group("Files", layout="monadtall", label=" "),
    Group("Discord", layout="monadtall", label="ﭮ",
            matches = [Match(wm_class=["discord"])]),
    Group("System", layout="monadtall", label="  "),
]
