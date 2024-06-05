import tkinter as tk
from tkinter import ttk
from calculator import Calculator
import webbrowser

class CalculatorGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")
        self.create_widgets()
        self.calculator = Calculator()

    def create_widgets(self):
        self.master.title("Calculator")
        self.master.geometry("620x400")
        self.master.resizable(False, False)
        self.master.configure(bg='#F3F3F3')

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 16), padding=(2, 4))
        self.style.configure("TLabel", font=("Helvetica", 20), background="#F3F3F3", foreground="black")

        self.display = tk.Entry(self, font=("Helvetica", 24), justify="right", bd=10, insertwidth=2, width=14, borderwidth=4, bg='#FFFFFF', fg='black')
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

        buttons = [
            ('C', 1, 0), ('⌫', 1, 1), ('', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

        self.signature_label = tk.Label(self, text="Developed by Thalles-J-G-Silva", cursor="hand2", bg='#F3F3F3', fg='blue')
        self.signature_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab("https://github.com/Thalles-JG-Silva"))
        self.signature_label.grid(row=6, column=0, columnspan=4, pady=10)

        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, column):
        if text != '':
            button = ttk.Button(self, text=text, command=lambda: self.on_button_click(text), style="TButton")
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

            if text in {'/', '*', '-', '+', '=', 'C', '⌫', '+/-'}:
                button.configure(style="Operator.TButton")

            self.style.configure("Operator.TButton", font=("Helvetica", 16), background="#E0E0E0", foreground="#000000")
            self.style.map("Operator.TButton",
                           background=[('active', '#D3D3D3')])

            if text == '=':
                button.configure(style="Equal.TButton")
                self.style.configure("Equal.TButton", font=("Helvetica", 16), background="#4CAF50", foreground="#000000")  # Change foreground to black
                self.style.map("Equal.TButton",
                               background=[('active', '#45A049')])

    def on_button_click(self, char):
        if char == 'C':
            self.calculator.clear()
            self.display.delete(0, tk.END)
        elif char == '⌫':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
            self.calculator.current_input = self.display.get()
        elif char == '=':
            result = self.calculator.calculate()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        elif char == '+/-':
            current = self.display.get()
            if current.startswith('-'):
                self.display.delete(0, tk.END)
                self.display.insert(0, current[1:])
                self.calculator.current_input = self.display.get()
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, '-' + current)
                self.calculator.current_input = self.display.get()
        else:
            self.calculator.input(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.calculator.current_input)

def start_gui():
    root = tk.Tk()
    app = CalculatorGUI(master=root)
    app.mainloop()
