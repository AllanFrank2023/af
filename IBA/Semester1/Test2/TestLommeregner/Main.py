import tkinter as tk
import Calculator
import Graphics

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.graphics = Graphics(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    main_app = main()
