import os
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

# Group configuration
groups = [
    Group("Dev", layout="monadtall", label=""),
    Group("Files", layout="monadtall", label=""),
    Group("Web", layout="floating", label="爵"),
    Group("System", layout="monadtall", label=""),
]
