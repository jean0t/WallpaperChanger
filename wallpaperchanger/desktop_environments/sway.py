from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error

class SwayEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # must be absolute
		try:
			run(["swaybg", "-i", path.__str__(), "-m", "fill"], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperSway)
