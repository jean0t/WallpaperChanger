from wallpaperchanger.desktop_environments.kde import KdeEnvironment
from wallpaperchanger.desktop_environments.gnome import GnomeEnvironment
from wallpaperchanger.desktop_environments.xfce import XfceEnvironment
from wallpaperchanger.desktop_environments.lxqt import LxqtEnvironment
from wallpaperchanger.desktop_environments.cinnamon import CinnamonEnvironment
from wallpaperchanger.desktop_environments.sway import SwayEnvironment
from wallpaperchanger.desktop_environments.hyprland import HyprlandEnvironment
from wallpaperchanger.desktop_environments.unknown import UnknownEnvironment
from wallpaperchanger.discover_de import Discover
from pathlib import PosixPath


# To Do: Not all desktop environments are Implemented yet
DESKTOP_ENVIRONMENT_MAP = {
# kde
"kde": KdeEnvironment,

# gnome
"gnome": GnomeEnvironment,

# xfce
"xfce": XfceEnvironment,
"xfce4": XfceEnvironment,

# lxqt
"lxqt": LxqtEnvironment,

# cinnamon
"cinnamon": CinnamonEnvironment,
"x-cinnamon": CinnamonEnvironment,

# sway
"sway": SwayEnvironment,

# hyprland
"hyprland": HyprlandEnvironment,

# i3
"i3": I3Environment
}


def main(wallpaper_path: PosixPath) -> None:
	desktop = Discover().lower()
	changer = DESKTOP_ENVIRONMENT_MAP.get(desktop, UnknownEnvironment)()

	# to_do: complete the main function
	pass
