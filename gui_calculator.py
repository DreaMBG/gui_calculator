import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.resizable(0, 0)

        self.current_input = ""
        self.result = None

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="sunken", justify="right")
        self.display.pack(expand=True, fill="both")

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            if len(button) == 4:
                colspan = button[3]
            else:
                colspan = 1

            ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
            buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                self.result = str(eval(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.result)
                self.current_input = self.result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current_input = ""
        elif char == "C":
            self.current_input = ""
            self.display.delete(0, tk.END)
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)

if __name__ == "__main__":
    Calculator().mainloop()