# Touhou Labyrinth 2 Save Converter

This repository provides a Python script that converts your saves from the DLSite version's format to the Steam version's format. At the top of the file are two variables that allow you to control where the save file to be converted is, and whether you want to fully unlock map data, fully erase map data, or transfer your map progress.

For a more in-depth look at the new save file format, please refer to [this pastebin](https://pastebin.com/Mpx7wdSg). 

## Installing Python

The script requires Python to be installed in your computer. Python is a scripting programming language, and what you need to install is its interpreter. You can then use the interpreter to run any scripts you download. Installing and running Python in Windows is easy:

* Head over to https://www.python.org/downloads/ and download Python 3.9 (or any other release >= 3.6)
* Make sure you click the option to add Python to your system's PATH
* Optionally, install the "py launcher" module to easily run python scripts
* Download this repository's source code through Github
  * There should be a "Download ZIP" option in the page, inside the "Code" dropdown button
* If you installed the py launcher, simply double click .py files to run them
  * You can also open a CMD and type "python anyfile.py" from a directory
  * On CMD, you can move around directories using the "cd" command
    * For example, "cd C:\Users\username\Downloads" should put you in your Downloads directory

If you're running Linux, please refer to your distribution's Python installation instructions. Chances are you already have Python 3.x installed by default!

## How to Use

The script `convert_save.py` must be copied into the directory of the save file you want to convert (for example, inside the save2 or save3 directory). There is a variable at the top of the script to control an option: `useFullMaps`. You can open the script in any text editor to edit it as needed:

* `useFullMaps` should be set to `None` (the default value) to carry over your map progress from the old save file format. Set it to `True` to fully unlock all map progress for every floor. You can set it to `False` to fully erase all map progress, too.

After copying the script into the directory, simply double click it (or run it via cmd, see install instructions above) to run it. After the script runs, you will find two files in your save directory: `result-decrypted.dat` and  `result.dat`.

* `result.dat` is the save file you'll use for the Steam version. It is already encrypted and can be used by simply renaming it to `save1.dat` (or similar) and moving it to the Steam save directory.
  * Your Steam save file should be in `%APPDATA%/CUBETYPE/tohoLaby`
  * If you rename it to `save1.dat`, make sure you already have a `save1.dat` to replace the new file with
    * If you don't already have a `save1.dat`, the game won't recognize the new save
  * Note that the save file preview the game shows you is only updated AFTER you load the save and then save in-game.
    * This happens because the game is the one that keeps track of the preview now, not the save file

* `result-decrypted.dat` is the same file as above, but fully decrypted if you want to look at the data on a hex editor.
  * It's mainly used for troubleshooting, so you can kinda ignore it if you just want to convert things
