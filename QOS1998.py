import tkinter as tk
import random
from tkinter import messagebox

class Qos:
    def __init__(self, root):
        self.root = root
        self.root.title("Qos - 1998 Edition")
        self.root.geometry("800x600")
        
        self.create_taskbar()
        self.create_desktop()

    def create_taskbar(self):
        taskbar = tk.Frame(self.root, bg="grey", height=30)
        taskbar.pack(side=tk.BOTTOM, fill=tk.X)

        start_button = tk.Button(taskbar, text="Start", command=self.show_start_menu, font=('Arial', 10))
        start_button.pack(side=tk.LEFT)

    def create_desktop(self):
        desktop = tk.Frame(self.root, bg="teal")
        desktop.pack(fill=tk.BOTH, expand=True)
        
        notepad_icon = tk.Button(desktop, text="Notepad", command=self.open_notepad, font=('Arial', 10))
        notepad_icon.place(x=50, y=50)

        calculator_icon = tk.Button(desktop, text="Calculator", command=self.open_calculator, font=('Arial', 10))
        calculator_icon.place(x=150, y=50)

        virus_icon = tk.Button(desktop, text="Virus.exe", command=self.trigger_gdi_hell, font=('Arial', 10))
        virus_icon.place(x=250, y=50)

    def show_start_menu(self):
        messagebox.showinfo("Start Menu", "This is the start menu of Qos!")

    def open_notepad(self):
        notepad = tk.Toplevel(self.root)
        notepad.title("Notepad")
        text = tk.Text(notepad, font=('Courier New', 10))
        text.pack(fill=tk.BOTH, expand=True)

    def open_calculator(self):
        calculator = tk.Toplevel(self.root)
        calculator.title("Calculator")
        
        display = tk.Entry(calculator, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        display.pack()

        button_frame = tk.Frame(calculator)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '4', '5', '6', '1', '2', '3', '0'
        ]

        for i, text in enumerate(buttons):
            button = tk.Button(button_frame, text=text, padx=20, pady=20, font=('Arial', 18),
                               command=lambda t=text: display.insert(tk.END, t))
            button.grid(row=i//3, column=i%3)

    def trigger_gdi_hell(self):
        self.melt_desktop()
        self.gdi_hell_effect()

    def melt_desktop(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
            else:
                for child in widget.winfo_children():
                    widget = child
                    self.melt_effect(widget)

    def melt_effect(self, widget):
        x, y, width, height = widget.winfo_x(), widget.winfo_y(), widget.winfo_width(), widget.winfo_height()
        new_y = y + random.randint(5, 15)
        if new_y < self.height:
            widget.place(x=x, y=new_y, width=width, height=height)
            self.root.after(100, lambda: self.melt_effect(widget))
        else:
            widget.place_forget()

    def gdi_hell_effect(self):
        for _ in range(50):  # Number of shapes per frame
            x0 = random.randint(0, self.width)
            y0 = random.randint(0, self.height)
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            color = random.choice(["red", "green", "blue", "yellow", "white", "black", "pink", "cyan", "magenta"])
            shape_type = random.choice(["rectangle", "oval", "line"])

            if shape_type == "rectangle":
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)
            elif shape_type == "oval":
                self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)
            elif shape_type == "line":
                self.canvas.create_line(x0, y0, x1, y1, fill=color, width=3)
        
        # Refresh the canvas
        self.root.after(100, self.gdi_hell_effect)

if __name__ == '__main__':
    root = tk.Tk()
    app = Qos(root)
    root.mainloop()
