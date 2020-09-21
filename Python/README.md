## Source Project:

Raschio Office Word 2019, v.4. This is a text editing program I made a while back.

## Industry:

Business.

## Changes:

Got rid of unused imports, made the code PEP-8 compliant, and added printing support for Linux.

## How to Run:

On Linux: Install TkInter with `sudo apt install python3-tk`, then run script with `~/$ python3 <script>`

On Mac: ¯\\\_(ツ)\_/¯. I'm pretty sure you run it like on Linux, but don't quote me on this.

On Windows: First, [Install Python.](https://www.python.org/downloads/windows/) Once you've done that, access your terminal and type `python <script>`.

## Program Logic:

```
| - Start
|
Enter GUI class
    | - Initialize window, bind inputs to various functions.
    | - Begin main loop
        | - Process inputs, run appropriate methods
            | - If <ctrl-p> || "Print" menu option:
                | - Figure out what OS.
                | - If Windows:
                    | - Print via default option
                | - If Linux:
                    | - Print via CUPS
                | - If MacOS:
                    | - Display error message
            | - If (<ctrl-s> && have not saved yet) || <ctrl-shift-s> || "Save as" menu option"
                | - Ask for filename to write to
                | - Get data from editor field
                | - Write to file
                | - Display confirmation
            | - If (<ctrl-s> && have already saved) || "Save" menu option"
                | - Get data from editor field
                | - Write to file
                | - Display confirmation
            | - If (<ctrl-o>) || "Open" menu option
                | - Ask for filename to open
                | - If file exists
                    | - Open file
                    | - Read from file
                    | - Set editor text to contents of file
                | - Else:
                    | - Display error message
            | - If (<ctrl-h>) || "Help" menu option
                | - Display help message
        | - Repeat
    | - Run destructor methods.
    /
   /
  /
 /
/
| - End program.
