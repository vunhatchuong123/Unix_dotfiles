import os
from libqtile import layout
from libqtile.config import Match
from .widgets import colors


base_layout_theme = {
    "border_width": 2,
    "border_focus": colors["blue"],
    "border_normal": colors["overlay0"],
}
non_floating_layout_theme = {
    **base_layout_theme,
    "margin": 8,
}

# Layout configuration
layouts = [
    # layout.Bsp(),
    # layout.Columns(),
    #layout.Floating(**non_floating_layout_theme),
    # layout.Matrix(),
    layout.Max(),
    layout.MonadTall(**non_floating_layout_theme),
    #layout.MonadWide(**non_floating_layout_theme),
    # layout.RatioTile(),
    # layout.Stack(num_stacks=2),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    **base_layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="flameshot"),  # Flameshot
        Match(wm_class="pavucontrol"),  # PulseAudio volume control applet
        Match(wm_class="blueman-manager"),  # Blueman applet
        Match(title="pinentry-gnome3"),  # GPG key password entry
    ]
)
