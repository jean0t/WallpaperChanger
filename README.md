# WallpaperChanger
***
The goal of this repository is to provide a full fledge application to linux desktops to change wallpapers agnostic to Desktop Environment. But It will need dependencies depending on the Desktop Environment used.

## Dependencies

Available soon...

## How the Project is Organized

Strategy Pattern was the choice for this project.  
**Why?**  
It uses the same pattern for implementing a class, set\_wallpaper() that will only differ in the desktop environment used. To make the implementation consistent and organized that pattern was chosen.  

***

1. We start by implementing an abstract class DesktopEnvironment with the method set\_wallpaper, this will force all other derived classes to follow its model.  
2. Then we implement the classes for each desktop environment.  
3. The file discover\_de.py will hold the function Discover() that is responsible to dynamically discover the desktop environment used.  
4. main.py will be the file haboring the main function with all its logic and the starting point for the program.  
5. run.py is the file responsible to provide the cli interface.

***

tree of the project:  
wallpaperchanger/  
├── desktop\_environments/  
│   ├── base.py  
│   ├── gnome.py  
│   ├── \_\_init\_\_.py  
│   ├── kde.py  
│   ├── sway.py  
│   ├── unknown.py  
│   └── xfce.py  
├── discover\_de.py  
└── main.py  

## License

GPL-3

## Contributions

Feel free to send pull requests or to fork the project, I will be very happy to have more people into it.

## TO DO
_really ambitious :P_  
- [ ] refactor to no third party dependencies
