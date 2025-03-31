from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error

class LxqtEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # must be absolute path
		try:
			run(["pcmanfm", "--set-wallpaper", path.__str__()], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperLxqt)
