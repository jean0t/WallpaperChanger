from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from subprocess import run, CalledProcessError
from pathlib import PosixPath
from wallpaperchanger.desktop_environments.error import Error

class XfceEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path: PosixPath): # must be absolute path
		try:
			run(["xfconf-query", "--channel", "xfce4-desktop", "--property", "/backdrop/screen0/monitor0/image-path", "--set", path.__str__()], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperXfce)
