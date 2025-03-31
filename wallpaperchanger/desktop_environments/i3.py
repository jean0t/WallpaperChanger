from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error

class I3Environment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # must be absolute path
		try:
			run(["feh", "--bg-scale", path.__str__()], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperI3)
