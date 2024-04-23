import tkinter as tk
from tkinter import filedialog
import tkinter.font
from tkinter import messagebox


# Add the "Format" menu to the menu bar
class TextEditor:
    def __init__(self, root):
        # Create the main text widget
        self.text = tk.Text(root, wrap=tk.NONE)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



        # Create a horizontal scrollbar for the Text widget
        self.scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.text.xview)
        self.text.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)


        # Create a vertical scrollbar for the Text widget
        self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.text.yview)
        # Configure the Text widget to use the scrollbar
        self.text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        # Create a menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Create a File menu with Open, Save, and Exit items
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.on_save_click)
        self.file_menu.add_command(label="New", command=self.clear_text)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)


        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_checkbutton(label="Bold", command=self.toggle_bold)
        self.format_menu.add_checkbutton(label="Italic", command=self.toggle_italic)
        self.format_menu.add_checkbutton(label="Underline", command=self.toggle_underline)

        # Create a submenu for font selection
        self.font_menu = tk.Menu(self.format_menu, tearoff=0)
        self.font_menu.add_command(label="Arial", command=lambda: self.set_font("Arial"))
        self.font_menu.add_command(label="Helvetica", command=lambda: self.set_font("Helvetica"))
        self.font_menu.add_command(label="Courier", command=lambda: self.set_font("Courier"))
        self.font_menu.add_command(label="Modern", command=lambda: self.set_font("Modern"))
        self.font_menu.add_command(label="Roman", command=lambda: self.set_font("Roman"))
        self.font_menu.add_command(label="Batang", command=lambda: self.set_font("Batang"))
        self.font_menu.add_command(label="Cambria", command=lambda: self.set_font("Cambria"))
        self.font_menu.add_command(label="Consolas", command=lambda: self.set_font("Consolas"))
        self.format_menu.add_cascade(label="Font", menu=self.font_menu)

        # Create the font menu

        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About LineEdit", command=self.about)

       
    def open_file(self):
        # open a file dialog and get the selected file's path
        filepath = filedialog.askopenfilename()

        # open the file and read its contents
        with open(filepath, 'r') as f:
            contents = f.read()

        # display the contents in the text area
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, contents)

    def set_font(self, font):
            # Set the font for the text widget
        self.text.config(font=font)

    def on_save_click(self):
            # Open the save file dialog
        filepath = filedialog.asksaveasfilename()
        if filepath:
                # Save the contents of the Text widget to the selected file
            with open(filepath, "w") as f:
                f.write(self.text.get("1.0", "end"))

    def toggle_bold(self):
        # Get the current selection
        start, end = self.text.tag_ranges("sel")

        # If there is a selection, toggle the bold tag
        if start:
            if self.text.tag_names("sel.first") == ("sel", "bold"):
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = tkinter.font.Font(weight="bold")
                self.text.tag_configure("bold", font=bold_font)


    def toggle_italic(self):
        # Get the current selection
        start, end = self.text.tag_ranges("sel")

        # If there is a selection, toggle the italic tag
        if start:
            if self.text.tag_names("sel.first") == ("sel", "italic"):
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = tkinter.font.Font(slant="italic")
                self.text.tag_configure("italic", font=italic_font)

    def toggle_underline(self):
        # Get the current selection
        start, end = self.text.tag_ranges("sel")


        # If there is a selection, toggle the underline tag
        if start:
            if self.text.tag_names("sel.first") == ("sel", "underline"):
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = tkinter.font.Font(underline=1)
                self.text.tag_configure("underline", font=underline_font)

    def clear_text(self):
       # Clear the content of the Text widget
       self.text.delete(1.0, tk.END)

    def about(self):
        messagebox.showinfo("About LineEdit", "LineEdit is a simple text editor made by Meggatgithub and Jishnugb. for more info, visit LineEdit's GitHub repository:") 






# Create the root window
root = tk.Tk()
root.title("LineEdit")
# Create the text editor
editor = TextEditor(root)




root.mainloop()
