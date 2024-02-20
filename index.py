import tkinter as tk
from tkinter import ttk

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker App")

        self.palette = {
            'Red': '#FF0000',
            'Green': '#00FF00',
            'Blue': '#0000FF',
            'Absolute Zero': '#0048ba',
            'Purple': '#800080',
            'Orange': '#FFA500',
            'Pink': '#FFC0CB',
            'Black': '#000000',
            'Cyan': '#00FFFF',
            'Ash Grey': '#b2beb5'
        }

        self.create_widgets()

    def create_widgets(self):
        self.color_label = ttk.Label(self.root, text="Choose a color:")
        self.color_label.grid(row=0, column=0, pady=10)

        self.color_combobox = ttk.Combobox(self.root, values=list(self.palette.keys()))
        self.color_combobox.grid(row=0, column=1, pady=10)

        self.pick_button = ttk.Button(self.root, text="Pick Color", command=self.pick_color)
        self.pick_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.color_canvas = tk.Canvas(self.root, width=100, height=50, bg='white')
        self.color_canvas.grid(row=2, column=0, columnspan=2, pady=10)

    def pick_color(self):
        selected_color = self.color_combobox.get()
        if selected_color in self.palette:
            hex_code = self.palette[selected_color]
            self.color_canvas.config(bg=hex_code)
        else:
            self.color_canvas.config(bg='white')

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()