from wallpaperchanger.main import main as execute
from pathlib import Path
from argparse import ArgumentParser

def main():
	parser = ArgumentParser(description="Changes the wallpaper")
	parser.add_argument("wallpaper_path", type=Path, help="Path to the wallpaper")
	args = parser.parse_args()

	if args.wallpaper_path.exists():
		execute(args.wallpaper_path.absolute())
	else:
		exit(1)

if __name__ == "__main__":
	main()
