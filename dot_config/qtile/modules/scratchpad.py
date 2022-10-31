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

    DropDown("chezmoi",
             terminal + " -e 'chezmoi' cd ",
             height=0.5,
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
    Key([mod], "i", lazy.group['scratchpad'].dropdown_toggle('chezmoi')),
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('ranger')),

])

