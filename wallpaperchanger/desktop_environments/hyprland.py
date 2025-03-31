from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error

class HyprlandEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # must be an absolute path
		try:
			run(["hyprpaper", path.__str__()], check=True)

		except CalledProcessError:
			print(Error.FailedToSetWallpaperHyprland)
