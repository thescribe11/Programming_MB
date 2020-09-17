import os
import tempfile
import threading  # TODO: Make up my mind whether or not I want to try threading this.
import platform

import tkinter as tk
from tkinter import messagebox, filedialog

import cups  # For printing stuff

filename = "unsaved.txt"

## Sometimes global variables really are the best way to go after all.
HELP_MESSAGE = """To save: click the "Save" button or type <<Ctrl+s>>, and follow instructions.

To save using alternate format: Click the "Save as..." button or type <<Ctrl+Shift+S>>, same procedure as saving.

To open a file: Click the "Open" button or type <<Ctrl+O>>, and follow instructions.

To print: click the "Print" button, or type <<Ctrl+P>>."""


def gettext(filename):
    x = ""
    try:
        with open(filename, 'r') as f:
            x = f.read()

    finally:
        return x


class MainGui:
    def __init__(self):
        self.my_filetypes = [("Text Format", '.txt'), ('All files', '.*')]

        self.root = tk.Tk()  # Main window and configs.
        self.root.configure(background="#E8E0E0")
        self.mainFrame = tk.Frame(self.root, width=680, height=600)
        self.mainFrame.grid(row=1, column=1, padx=50, pady=30)
        self.root.title("Raschio Office Word 2019")

        self.mainFrame.columnconfigure(0, weight=10)  # Makes frame that holds self.texter.
        self.mainFrame.rowconfigure(0, weight=10)
        self.mainFrame.grid_propagate(False)

        self.texter = tk.Text(self.mainFrame, font="Times 14 bold")  # Self.texter and configs.
        self.texter.grid(row=0, column=0, sticky="nsew")

        self.texter.bind('<KeyRelease>', self.get_text)  # Keybinds.
        self.texter.bind('<Control-s>', self.saver)
        self.texter.bind('<Control-S>', self.super_saver)
        self.texter.bind("<Control-o>", self.openner)
        self.texter.bind("<Control-p>", self.printer)

        self.menu = tk.Menu(self.root, activeborderwidth=3, font="Times")  # Menu.
        self.menu.add_command(label="Save", command=self.saver)
        self.menu.add_command(label="Save as...", command=self.super_saver)
        self.menu.add_command(label="Open", command=self.openner)
        self.menu.add_command(label="Help", command=self.YOU_DUMMY)
        self.menu.add_command(label="Print", command=self.printer)

        self.root.config(menu=self.menu)  # Adding menu to window.

        self.scroll = tk.Scrollbar(self.mainFrame)  # Creating the Scrollbar.
        self.scroll.grid(row=0, column=1, sticky="nes")
        self.scroll.config(command=self.texter.yview)  # Attaching scroll to texter.
        self.texter.config(yscrollcommand=self.scroll.set)

        self.texter.focus()

        self.root.mainloop()

    def get_text(self, *args):
        self.current_text = self.texter.get("1.0", "end-1c")

    def saver(self, *args):
        global filename
        if filename == "unsaved.txt":
            filename = filedialog.asksaveasfilename(parent=self.root,
                                                    initialdir=os.getcwd(),
                                                    title="Please select a file name for saving:",
                                                    filetypes=self.my_filetypes)
        tester = filename.strip()
        if not (tester[-4] == '.' and tester[-3] == 't' and tester[-2] == 'x' and tester[-1] == 't'):
            filename = filename + ".txt"

        self.current_text = self.texter.get("1.0", "end-1c")
        with open(filename, 'w') as f:
            f.write(self.current_text)

        messagebox.showinfo("Information", "Text was succsessfully saved.")

    def super_saver(self, *args):
        global filename
        filename = "unsaved.txt"
        self.saver()

    def openner(self, *args):
        global filename

        filename = filedialog.askopenfilename(parent=self.root,
                                              initialdir=os.getcwd(),
                                              title="Please select a file:",
                                              filetypes=self.my_filetypes)

        file_text = str(gettext(filename))

        self.texter.delete('1.0', 'end')
        self.texter.insert("1.0", file_text)

    def printer(self, *args):
        global filename
        file = tempfile.mktemp("asdf.txt")
        with open(file, "w+") as f:
            self.current_text = self.texter.get("1.0", "end-1c")
            f.write(self.current_text)

        if (operating_system := platform.system()) == "Windows":
            os.startfile(file, "print")  # Makes use of Notepad, since accessing printers is a @%$# on Windows.
        elif operating_system == "Linux":
            conn = cups.Connection()
            printers = conn.getPrinters()
            printer_name = list(printers.keys())[0]
            conn.printFile(printer_name, file, filename, {})
        elif operating_system == "Darwin":
            ## Sorry about the weird alignment; PEP-8 strikes again.
            messagebox.showinfo("Printing Error",
                                'Unfortunately, Raschio Office Word does not support printing on Mac.')

    @staticmethod
    def YOU_DUMMY(self, *args):
        messagebox.showinfo("Help", HELP_MESSAGE)

if __name__ == "__main__":
    MainGui()
