import os
from libqtile import widget, qtile, bar
from .keys import terminal

import colors

icons_path = os.path.expanduser("~") + "/.config/qtile/assets/catppuccin_icons"

# Theme configuration
colors = colors.catppuccin()

# Widget configuration
widget_defaults = dict(
    font="JetBrainsMono Nerd Font, Medium",
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
            foreground=colors["mauve"],
            margin=7,
            fontsize=30,
        ),
        widget.TextBox(
            text = "",
            padding = 8,
            foreground=colors["surface2"],
            fontsize=25,
            ),
       # widget.Spacer(
       #     length = 20,
       # ),
        widget.GroupBox(
            fontsize                    = 23,
            margin_y                    = 3,
            margin_x                    = 5,
            borderwidth                 = 2,
            active                      = colors["green"],
            block_highlight_text_color  = colors["red"],
            inactive                    = colors["sapphire"],
            rounded                     = True,
            disable_drag                = True,
            highlight_color=colors["surface0"],
            highlight_method="line",
            this_current_screen_border=colors["pink"],
            this_screen_border=colors["rosewater"],
            other_screen_border=colors["surface0"],
            other_current_screen_border=colors["surface0"],
        ),
        widget.TextBox(
            text = "",
            offset = 4,
            padding = 4,
            foreground=colors["surface2"],
            fontsize= 25,
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

        widget.Clock(
            format="%A %d-%m-%Y %H:%M",
            fontsize = 15,
        ),
        widget.Spacer(), 
        widget.TextBox(
          text = '',
          fontsize = 20,
        ),
        widget.DF(
          fontsize = 15,
          format = ' {f} GB  ',
          partition = '/',
          mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('bleachbit')},
          visible_on_warn = False,
          warn_color = colors["red"],
        ),
        widget.Sep(
          linewidth = 2,
          background=colors["crust"],
        ),
        widget.TextBox(
            text = '  ',
            fontsize = 20,
        ),
        widget.CheckUpdates(
            fontsize = 15,
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
        widget.TextBox(
            text = '墳 ',
            fontsize = 20,
            foreground  = colors["blue"],
        ),
        widget.PulseVolume(
            foreground  = colors["blue"],
            fontsize    = 15,
            padding     = 0,
        ),
# Doesn't work  if there is no batt
#        widget.Image(
#            filename  = '~/.config/qtile/assets/bar/bat.png',
#            margin    = 7
#        ),         
#        widget.Battery(format=' {percent:2.0%}',
#            foreground  = colors["red"],
#            fontsize    = 12,
#            padding     = 0,
#        ),  
        widget.Spacer(
            length = 30,
        ),
        widget.Spacer(
            length      = 10,
        ), 
# Systray actually on this line
        widget.TextBox(
            text = "",
            offset = 4,
            padding = 4,
            foreground=colors["surface2"],
            fontsize= 25,
        ),
        widget.TextBox(
            text = " ",
            margin = 8,
            foreground=colors["red"],
            fontsize= 20,
            mouse_callbacks  = {
                'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/bin/powermenu'))
            }
        ),
        widget.Spacer(
            length = 10,

        ),
    ]
    if primary:
        widgets.insert(
            -4,
            widget.Systray(
                icon_size   = 24,
                padding     = 0,
                background  = colors["surface0"]
            ),
        )
    return widgets
