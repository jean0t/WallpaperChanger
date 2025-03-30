from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from wallpaperchanger.desktop_environments.error import Error
from pathlib import PosixPath

class CinnamonEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # the path must be absolute
		try:
			run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", f"file://{path.__str__()}], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperCinnamon)
