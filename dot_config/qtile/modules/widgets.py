import os
from libqtile import widget
from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

icons_path = os.path.expanduser("~") + "/.config/qtile/qtile_icons"
CMD_DICT['popOS'] = '("sudo apt update",0)'
# Theme configuration
# Catppuccin Macchiato colors (https://github.com/catppuccin/catppuccin)
colors = {
    "rosewater": ["#f4dbd6"],
    "flamingo": ["#f0c6c6"],
    "pink": ["#f5bde6"],
    "mauve": ["#c6a0f6"],
    "red": ["#ed8796"],
    "maroon": ["#ee99a0"],
    "peach": ["#f5a97f"],
    "yellow": ["#eed49f"],
    "green": ["#a6da95"],
    "teal": ["#8bd5ca"],
    "sky": ["#91d7e3"],
    "sapphire": ["#7dc4e4"],
    "blue": ["#8aadf4"],
    "lavender": ["#b7bdf8"],
    "text": ["#cad3f5"],
    "subtext1": ["#b8c0e0"],
    "subtext0": ["#a5adcb"],
    "overlay2": ["#939ab7"],
    "overlay1": ["#8087a2"],
    "overlay0": ["#6e738d"],
    "surface2": ["#5b6078"],
    "surface1": ["#494d64"],
    "surface0": ["#363a4f"],
    "base": ["#24273a"],
    "mantle": ["#1e2030"],
    "crust": ["#181926"],
}

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
    powerline_arrow_left = {"decorations": [PowerLineDecoration()]}
    powerline_arrow_right = {"decorations": [PowerLineDecoration(path="arrow_right")]}
    widgets = [
        widget.Sep(linewidth=0, padding=10, background=colors["flamingo"]),
        widget.TextBox(
            text="",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
            foreground=colors["crust"],
            background=colors["flamingo"],
            padding=8,
            fontsize=28,
            **powerline_arrow_left
        ),
        widget.Sep(linewidth=0, padding=8, background=colors["crust"]),
        widget.GroupBox(
            fontsize=28,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            borderwidth=1,
            active=colors["blue"],
            inactive=colors["overlay0"],
            rounded=False,
            highlight_color=colors["surface2"],
            highlight_method="line",
            this_current_screen_border=colors["blue"],
            this_screen_border=colors["surface2"],
            other_current_screen_border=colors["pink"],
            other_screen_border=colors["surface2"],
            foreground=colors["pink"],
            background=colors["base"],
            **powerline_arrow_left
        ),
        widget.CurrentLayoutIcon(
            foreground=colors["crust"],
            background=colors["flamingo"],
            padding=10,
            scale=0.8,
            custom_icon_paths=[icons_path + "/catppuccin-Macchiato-Crust"],
            **powerline_arrow_left
        ),
        widget.WindowName(
            foreground=colors["text"],
            background=colors["base"],
            padding=8,
            max_chars=50,
            width=400,
            **powerline_arrow_left
        ),
        widget.Prompt(
            foreground=colors["crust"],
            background=colors["red"],
            padding=8,
            **powerline_arrow_left
        ),
        widget.TextBox(
            text=' ',
            background="#e0def4",
            foreground="#191724",
            padding=2
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="popOS",
            display_format="{updates} Updates",
            colour_have_updates="#191724",
            mouse_callbacks= {
                'Button1':
                lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                },
            background="#e0def8"
        ),
        widget.TextBox(
            text='',
            background="#e0def4",
            foreground="#ea9a97",
            padding=-3,
            fontsize=38
        ),
        widget.Spacer(background=colors["crust"], **powerline_arrow_right),
        widget.Clock(
            foreground=colors["crust"],
            background=colors["flamingo"],
            padding=8,
            format="%Y-%d-%m %H:%M",
        ),
        widget.TextBox(
            text='',
            mouse_callbacks= {
                'Button1':
                lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                },
            background=colors["flamingo"],
            foreground=colors["crust"],
            padding=20,
                )
    ]
    if primary:
        widgets.insert(
            -2,
            widget.Systray(
                foreground=colors["blue"],
                # background=colors["base"],
                background=["#FFFFFF"],
                padding=2,
                **powerline_arrow_right
            ),
        )
    return widgets
