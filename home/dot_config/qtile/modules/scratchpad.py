from .keys import terminal, keys, mod
from .groups import groups
from libqtile.config import ScratchPad, DropDown, Key
from libqtile.command import lazy

# Configuration
height =				0.8
y_position =			0.1
opacity =				1

groups.append(ScratchPad("scratchpad", [
    DropDown("term",
             terminal,
             height=height,
             y=y_position,
             opacity=opacity),

    DropDown("ranger",
             terminal + " -e ranger",
             height=height,
             y=y_position,
             opacity=opacity),

    DropDown("lazygit",
             terminal,
             height=height,
             width=0.4,
             y=0.1,
             x=0.6,
             opacity=opacity),

    DropDown("chezmoi",
             terminal + " -e 'chezmoi' cd ",
             height=0.5,
             opacity=opacity),

    DropDown("kami",
             terminal + " -e kami",
             height=height,
             y=y_position,
             opacity=opacity),

#	DropDown("music",
#			terminal + " -e ncmpcpp",
#            height=height,
#            y=y_position,
#            opacity=opacity),
#
    #DropDown("volume", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),

]))

keys.extend([
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "g", lazy.group['scratchpad'].dropdown_toggle('lazygit')),
    Key([mod], "i", lazy.group['scratchpad'].dropdown_toggle('chezmoi')),
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key([mod, "shift"], "k", lazy.group['scratchpad'].dropdown_toggle('kami')),

])

