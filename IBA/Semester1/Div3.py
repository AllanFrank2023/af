import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Lommeregner")

        # Opret variabler
        self.expression = ""
        self.memory = 0

        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Knapper
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '=', '/'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Memory-knap
        tk.Button(root, text='M+', command=self.memory_store).grid(row=row, column=col)
        root.mainloop()

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Fejl"
        else:
            self.expression += button
        self.display_var.set(self.expression)
    
    def memory_store(self):
        try:
            self.memory = float(self.expression)
        except ValueError:
            self.expression = "Fejl"
        self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
