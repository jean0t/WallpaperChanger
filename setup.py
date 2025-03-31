from setuptools import setup, find_packages

setup(
	name="wallpaperchanger",
	version="0.1",
	description="A cross-desktop Environment wallpaper changer for Linux",
	author="jean0t",
	url="https://github.com/jean0t/WallpaperChanger",
	packages=find_packages(),
	py_modules=["run"],
	entry_points={
		"console_scripts": [
			"wallpaperchanger = wallpaperchanger.cli:main",
		],
	},
	license="GPL-3",
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3))",
		"Operating System :: POSIX :: Linux",
	],
)
