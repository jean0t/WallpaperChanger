from abc import ABC, abstractmethod


class DesktopEnvironment(ABC):
	"""
	Definition for the desktop environment classes
	provides a standard method to interact
	"""
	@abstractmethod
	def set_wallpaper(self):
		pass
