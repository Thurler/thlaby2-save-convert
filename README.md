# Touhou Labyrinth 2 Save Converter

This repository provides a Python script that converts your saves from the DLSite version's format to the Steam version's format. At the top of the file are two variables that allow you to control where the save file to be converted is, and whether you want to fully unlock map data or not.

Keep in mind that map progress CANNOT be carried over, since the format used by the developers changed. Everything else was kept somewhat similar, which makes it easy to carry over.

For a more in-depth look at the new save file format, please refer to [this pastebin](https://pastebin.com/Mpx7wdSg). 

## How to Use

The script `convert_save.py` has two variables at the top to control what is executed: `path` and `useFullMaps`. You can open the script in any text editor to edit it. Before running the script, make sure both variables have the correct value for what you want!

* `path` should be a complete path to the directory containing the save file you want to convert. 
  * Make sure the value uses forward slashes (`/`) instead of back slashes (`\`) if you're on Windows!
  * Tip for Windows users: you can select the full path for the current directory by clicking on the address bar in Windows Explorer!
    * Just make sure to replace the back slashes with forward slashes!

* `useFullMaps` should be set to `True` to fully unlock all map progress for every floor. You can set it to `False` to fully erase all map progress, too.

After the script runs, you will find two files in your save directory: `result-decrypted.dat` and  `result.dat`.

* `result.dat` is the save file you'll use for the Steam version. It is already encrypted and can be used by simply renaming it to `save1.dat` and moving it to the Steam save directory.
  * Your Steam save file should be in `%APPDATA%/CUBETYPE/tohoLaby`
  * If you rename it to `save1.dat`, make sure you already have a `save1.dat` to replace the new file with
    * If you don't already have a `save1.dat`, the game won't recognize the new save

* `result-decrypted.dat` is the same file as above, but fully decrypted if you want to look at the data on a hex editor.
  * It's mainly used for troubleshooting, so you can kinda ignore it

## Installing Python

The script requires Python to be installed in your computer. Python is a scripting programming language, and what you need to install is its interpreter. You can then use the interpreter to run any scripts you download. Installing and running Python in Windows is easy:

* Head over to https://www.python.org/downloads/ and download Python 3.9 (or any 3.x release)
* Make sure you click the option to add Python to your system's PATH
* Optionally, install the "py launcher" module to easily run python scripts
* Download this repository's source code through Github
* If you installed the py launcher, simply double click "convert_save.py"
  * You can also open a CMD and type "python main.py" from the directory you downloaded to
  * On CMD, you can move around directories using the "cd" command
    * For example, "cd C:\Users\username\Downloads" should put you in your Downloads directory

If you're running Linux, please refer to your distribution's Python installation instructions. Chances are you already have Python 3.x installed by default!
