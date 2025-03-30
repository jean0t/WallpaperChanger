from wallpaperchanger.desktop_environments.kde import KdeEnvironment
from wallpaperchanger.desktop_environments.gnome import GnomeEnvironment
from wallpaperchanger.desktop_environments.unknown import UnknownEnvironment
from wallpaperchanger.discover_de import Discover
from pathlib import PosixPath


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
"x-cinnamon": CinnamonEnvironment
}


def main(wallpaper_path: PosixPath) -> None:
	desktop = Discover().lower()
	changer = DESKTOP_ENVIRONMENT_MAP.get(desktop, UnknownEnvironment)()

	# to_do: complete the main function
