from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error


class GnomeEnvironment(DesktopEnvironment):
	def set_wallpaper(path: PosixPath): # must be absolute path
		try:
			run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{path.__str__()}"], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperGnome)
