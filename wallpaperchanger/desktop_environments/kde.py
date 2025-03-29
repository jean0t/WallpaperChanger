from wallpaperchanger.desktop_environments.base import DesktopEnvironment
from wallpaperchanger.desktop_environments.error import Error 
from subprocess import run, CalledProcessError

class KdeEnvironment(DesktopEnvironment):
	def set_wallpaper(self, path): # path must be absolute
		script = f"""
			var allDesktops = desktops();
			for (i=0; i<allDesktops.length; i++) {{
			    d = allDesktops[i];
			    d.wallpaperPlugin = "org.kde.image";
			    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
			    d.writeConfig("Image", "file://{str(path)}");
			}}
			"""
		try:
			run(["qdbus", "org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell.evaluateScript", script], check=True)
		except CalledProcessError:
			print(Error.FailedToSetWallpaperKde)
