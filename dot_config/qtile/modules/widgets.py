import os
from libqtile import widget, qtile, bar
from .keys import terminal

import colors

icons_path = os.path.expanduser("~") + "/.config/qtile/assets/catppuccin_icons"

# Theme configuration
colors = colors.catppuccin()

# Widget configuration
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=18,
    padding=6,
    bacground=colors["crust"],
)
extension_defaults = widget_defaults.copy()


def init_bar_widgets(primary=True):
    """Creates a list of widgets for use in QTile bar
    Parameters:
        primary (bool) : if true, will include the systrain and other main monitor widgets

    Returns:
        widgets (List(widget)) : a list of QTile widgets
    """
    widgets = [
        widget.Spacer(
            length = 10,
        ),
        widget.TextBox(
            text="",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
            foreground=colors["pink"],
            margin=7,
            fontsize=28,
        ),
        widget.Spacer(
            length = 20,
        ),
        widget.GroupBox(
            fontsize                    = 25,
            margin_y                    = 3,
            margin_x                    = 5,
            borderwidth                 = 1,
            font                        = "JetBrainsMono Nerd Font, Regular",
            active                      = colors["green"],
            block_highlight_text_color  = colors["red"],
            inactive                    = colors["sapphire"],
            rounded                     = True,
            disable_drag                = True,
            highlight_color=colors["surface0"],
            highlight_method="line",
            this_current_screen_border=colors["lavender"],
            other_current_screen_border=colors["blue"],
        ),
        widget.Sep(
            linewidth=0,
            padding=2,
            background=colors["sapphire"]
        ),
        widget.Spacer(
            length = 10,
        ), 
        widget.CurrentLayoutIcon(
           padding = 0,
           scale = 0.7,
           custom_icon_paths = [os.path.expanduser("~/.config/qtile/assets/layout")],
        ),
        widget.WindowName(
            foreground=colors["text"],
            background=colors["base"],
            fontsize=15,
            padding=8,
            max_chars=50,
            width=400,
        ),
        widget.Prompt(
            foreground=colors["crust"],
            background=colors["red"],
            padding=8,
        ),
        # ----------------------------------------

        widget.Spacer(
            length = bar.STRETCH,
        ),
        # ----------------------------------------
        widget.Spacer(
            length = 16,
        ), 
        widget.TextBox(
            text=' ',
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro = "Ubuntu",
            display_format = "{updates} Updates",
            colour_have_updates=colors["red"],
            no_update_string = 'No Updates',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo apt upgrade')},
            foreground=colors["text"],
            background=colors["base"],
            padding=5,
        ),
        widget.Spacer(
            length = 16,
        ),
        widget.Image(

            filename  = '~/.config/qtile/assets/bar/vol.png',
            margin    = 8,
            size      = 50,
        ),
        widget.Spacer(
            length = 16,
        ),
        widget.PulseVolume(
            font        = "JetBrainsMono Nerd Font, Regular",
            foreground  = colors["blue"],
            fontsize    = 15,
            padding     = 0,
        ),
        widget.Spacer(
            length = 30,
        ),
        widget.Spacer(
            length      =10,
            background  = colors["surface0"]
        ), 
# Systray actually on this line
       widget.Spacer(
            length      = 10,
            background  = colors["surface0"]
        ), 
        widget.Spacer(
            length = 20,
        ),  
        widget.Clock(
            font        = "JetBrainsMono Nerd Font, Regular",
            format="%Y-%d-%m %H:%M",
        ),
        widget.Image(
            filename         = '~/.config/qtile/assets/bar/power.png',
            margin           = 8,
            mouse_callbacks  = {
                'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
            }
        ),
        widget.Spacer(
            length = 10,

        ),
    ]
    if primary:
        widgets.insert(
            -5,
            widget.Systray(
                icon_size   = 24,
                padding     = 0,
                background  = colors["surface0"]
            ),
        )
    return widgets
