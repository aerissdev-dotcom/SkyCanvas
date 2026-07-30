# SkyCanvas
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ASCII constellation viewer powered by astronomical data.

SkyCanvas is a lightweight command-line tool that allows you to explore constellations directly in your terminal.
It renders constellations as ASCII art, displays astronomical data, compares different constellations, show currently visible constellations, and allows exporting them into image formats.

No internet connection is required after installation.

# Features

- ASCII constellation rendering
- Braille based terminal render
- Constellation information tables
- Stars and their connections visualised 
- Animated constellation drawing
- Comparing two constellations side by side
- Showing visible constellations for tonight
- Random constellations to discover
- Export constellation to PNG / JPG / BMP / SVG format
- Manual
- Lightweight and quite fast

# Installation

## Requirements

- Python 3.10+
- pip

Install SkyCanvas:
```bash
pip install skycanvas
```
Example:

![SkyCanvas Installation](https://raw.githubusercontent.com/aerissdev-dotcom/SkyCanvas/main/screenshots/skyCanvasInstall.gif)

Run:

```bash
skycanvas --help
```

# Commands

## version

Show SkyCanvas version.

```bash
skycanvas version
```

## man

Display the SkyCanvas manual.

```bash
skycanvas man
```

## constellation

Display the constellation ASCII art and info table of choice.

```bash
skycanvas constellation <name>
```

![SkyCanvas Constellation](https://raw.githubusercontent.com/aerissdev-dotcom/SkyCanvas/main/screenshots/skyCanvasConstellation.png)

## constellation --animate

Display animated version of ASCII art, and info table of choice.

```bash
skycanvas constellation <name> --animate
```
![SkyCanvas Constellation](https://raw.githubusercontent.com/aerissdev-dotcom/SkyCanvas/main/screenshots/skyCanvasConstellationAnimate.gif)

## compare

Compare two constellations.

```bash
skycanvas compare <name1> <name2>
```

![Skycanvas Compare](https://raw.githubusercontent.com/aerissdev-dotcom/SkyCanvas/main/screenshots/skyCanvasCompare.png)

## list

Display the list of available constellations.

```bash
skycanvas list
```

## tonight

Display constellations that are visible tonight.

```bash
skycanvas tonight
```

## --export

Export the chosen constellation or tonight constellations to an image format.

```bash
skycanvas --export crux svg
```

Available image formats:

- PNG
- JPG
- BMP
- SVG

Exports are stored in:

```
~/SkyCanvas/Exports/
```

## rand

Show a randomly choosen constellation.

```bash
skycanvas rand
```

## export-help

Display export usage information.

```bash
skycanvas export-help
```

## logo

Show a SkyCanvas logo.

```bash
skycanvas logo
```

# Data Storage

## SkyCanvas does not require any external database.

All constellation data is stored locally inside the tool.

No account or cloud synchronization requited whatsoever.

# Supported Constellations

# SkyCanvas currently includes many popular constellations:

- Orion
- Ursa Major
- Cassiopeia
- Scorpius
- Taurus
- Gemini
- Leo
- Cygnus
- Lyra
- Aquila
- Pegasus
- Andromeda
- Canis Major
- Canis Minor
- Draco
- Sagittarius
- Virgo
- Aries
- Capricornus
- Pisces
- Ursa Minor
- Perseus
- Cepheus
- Hydra
- Centaurus
- Crux
- Phoenix
- Libra
- Aquarius
- Cancer

# Technologies

## SkyCanvas is build with:

- Python
- Typer
- Rich
- Pillow
- Skyfield

# Files

```
skycanvas/

    - main.py
    - compare.py
    - constellations.py
    - coordinates.py
    - export.py
    - logo.py
    - render.py
    - tonight.py
```

# Development

## Clone repository:

```bash
git clone https://github.com/aerissdev-dotcom/SkyCanvas.git
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
skycanvas --help
```

# License

MIT License

# Author

aeriss-dev

GitHub:

https://github.com/aerissdev-dotcom

# Version

0.1.0

# Testing and developing OS

SkyCanvas was developed and tested on macOS.
The author does not guarantee full compatibility with every operating system.

# OS Compatibility

## macOS

Fully tested.

## Windows

Should work normally with Python installed.

## Linux

Should work normally, but terminal rendering might depend on terminal font support.

# Conclusion

SkyCanvas is a small terminal-based astronomy project I created to make exploring the constellations simple and enjoyable.









