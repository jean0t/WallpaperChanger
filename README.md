# WallpaperChanger 🖼️🚀

***  
The goal of this repository is to provide a full-fledged application for Linux desktops to change wallpapers, agnostic to the Desktop Environment. It will include dependencies based on the Desktop Environment used.  
***  

## Dependencies 🔧
**obs: if the desktop environment isn't listed here, consider that no dependency is needed**  
- **KDE:** Depends on `qdbus`  
- **I3:** Depends on `feh`
- **Sway and Hyprland:** Depends on `swaybg`

## How the Project is Organized 🗂️

The **Strategy Pattern** was chosen for this project.  
**Why?**  
It enforces the implementation of a common `set_wallpaper()` method that differs only in the desktop environment used, keeping the code consistent and organized.

***  

1. **Abstract Class:**  
   We start by implementing an abstract class `DesktopEnvironment` with the method `set_wallpaper()`, forcing all derived classes to follow its model.  
2. **Environment Classes:**  
   Then we implement the classes for each desktop environment.  
3. **Dynamic Discovery:**  
   The file `discover_de.py` holds the `Discover()` function responsible for dynamically detecting the desktop environment in use.  
4. **Main Logic:**  
   `main.py` contains the main function with all the logic and serves as the starting point for the program.  
5. **CLI Interface:**  
   `run.py` provides the command-line interface for the program.  
6. **Error Handling:**  
   `error.py` is located inside `desktop_environments` and provides a unified way to handle errors, making debugging easier without code duplication or hard-coded strings.

***  

## Project Tree 🌳

```
wallpaperchanger/
├── desktop_environments/
│   ├── base.py
│   ├── error.py
│   ├── gnome.py
│   ├── hyprland.py
│   ├── i3.py
│   ├── __init__.py
│   ├── kde.py
│   ├── lxqt.py
│   ├── sway.py
│   ├── unknown.py
│   └── xfce.py
├── discover_de.py
└── main.py
```

## License 📜

GPL-3

## Contributions 🤝

Feel free to send pull requests or fork the project. I'm always excited to have more people involved!  

## TO DO 📝

_Really ambitious 😄 :P_  
- [ ] Refactor to remove third-party dependencies
