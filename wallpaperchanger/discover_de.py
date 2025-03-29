from os import getenv

def Discover():
	"""
	Discover which Desktop environment is being used
	dynamically, otherwise returns unknown
	"""
	return getenv("XDG_CURRENT_DESKTOP") or getenv("DESKTOP_SESSION") or "unknown"
