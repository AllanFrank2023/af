import tkinter as tk

class Graphics:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create the input field
        self.entry = tk.Entry(root, textvariable=self.result_var, justify="right", font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create calculator buttons
        buttons = [
            '7', '9', '8', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            'sqrt', 'sin', 'cos', 'tan',
            '(', ')', '.'  # Added '(' and ')' buttons and the '.' button
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b), padx=20, pady=20, font=("Arial", 20)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == '=':
            self.calculate()
        elif button == 'C':
            self.result_var.set("0")
        else:
            current_text = self.result_var.get()
            if current_text == '0':
                current_text = ''
            current_text += button
            self.result_var.set(current_text)

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except:
            self.result_var.set("Error")

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Undefined"

    @staticmethod
    def square_root(a):
        return a ** 0.5

    @staticmethod
    def sine(angle):
        import math
        return math.sin(angle)

    @staticmethod
    def cosine(angle):
        import math
        return math.cos(angle)

    @staticmethod
    def tangent(angle):
        import math
        return math.tan(angle)

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.graphics = Graphics(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    main_app = Main()
