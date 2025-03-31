# WallpaperChanger 🖼️🚀

***  
The goal of this repository is to provide a full-fledged application for Linux desktops to change wallpapers, agnostic to the Desktop Environment. It will include dependencies based on the Desktop Environment used.  
***  

## Dependencies 🔧
**obs: if the desktop environment isn't listed here, consider that no dependency is needed**  
- **KDE:** Depends on `qdbus`  
- **I3:** Depends on `feh`
- **Sway:** Depends on `swaybg`
- **Hyprland:** Depends on `hyprpaper`

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


***

## Installation

You can install **WallpaperChanger** either by manually downloading the tarball from the releases page or by installing the `.whl` file generated from the source.

### **Option 1: Install from Tarball**

1. Download the latest tarball from the [Releases page](https://github.com/yourusername/wallpaperchanger/releases).
2. Extract the tarball:

   ```bash
   tar -xvzf wallpaperchanger-0.1.tar.gz
   ```

3. Navigate to the extracted folder:

   ```bash
   cd wallpaperchanger-0.1
   ```

4. Install the package:

   ```bash
   python setup.py install
   ```

### **Option 2: Install from .whl File**

If you prefer using the `.whl` (Wheel) file:

1. Download the `.whl` file from the [Releases page](https://github.com/jean0t/wallpaperchanger/releases) or build it using `python setup.py bdist_wheel`
2. Install the `.whl` file using `pip`:

   ```bash
   pip install *.whl
   ```

***

## Usage

To change your desktop wallpaper, simply run the `wallpaperchanger` script followed by the path to the image you want to set as the wallpaper.

### **Basic Command**

```bash
wallpaperchanger /path/to/your/wallpaper.jpg
```

This will automatically detect your desktop environment and set the wallpaper accordingly.

### **Example**

```bash
wallpaperchanger /home/user/Pictures/background.jpg
```

This will set the image at `/home/user/Pictures/background.jpg` as the wallpaper for your current desktop environment.

***

## License 📜

GPL-3

## Contributions 🤝

Feel free to send pull requests or fork the project. I'm always excited to have more people involved!  

## TO DO 📝

_Really ambitious 😄 :P_  
- [ ] Refactor to remove third-party dependencies
