import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

@hook.subscribe.restart
def cleanup():
    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))
    shutil.rmtree(os.path.expanduser('~/.config/qtile/modules/__pycache__'))

@hook.subscribe.shutdown
def killall():
    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))
    shutil.rmtree(os.path.expanduser('~/.config/qtile/modules/__pycache__'))
