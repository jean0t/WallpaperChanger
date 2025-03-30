from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from wallpaperchanger.desktop_environments.error import Error

class UnknownEnvironment(DesktopEnvironment):
	"""
	If it falls here, it means the desktop environment wasn't identified
	this class is simply a fallback
	"""
	def set_wallpaper(self):
		print(Error.UnknownDesktopSetWallpaper)
