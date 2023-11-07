import tkinter as tk
calc = __import__('11_1')


class calcGUI:

    def __init__(self):

       
        self.root = tk.Tk()

        self.root.geometry("500x800")
        self.root.title("Calc mean and standard deviation")

        self.title_label = tk.Label(self.root, text="Calculate: mean & standard deviation", font=('Ariel', 18))
        self.title_label.pack(padx = 20, pady = 20)

        self.explain_label = tk.Label(self.root, text="Enter numbers and seperate with space")
        self.explain_label.pack()

        self.imput_entry = tk.Entry(self.root, width=100, font=('Ariel', 24))
        self.imput_entry.pack(padx = 10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.columnconfigure(2, weight = 1)


        self.calc_button = tk.Button(self.root, text = "Calculate", font = ('Ariel', 18), command = self.calc)
        self.calc_button.pack(pady = 20)



        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady = 20)




        self.quit_button = tk.Button(self.root, text = "Quit", command = self.close)
        self.quit_button.place(x = 390, y = 740, height = 50, width = 100)
 
        self.root.mainloop()
    
    def calc(self):
        strnum_list = self.imput_entry.get().split()
        num_list = [ int(i) for i in strnum_list ]
        print(num_list)

        xbar = calc.mean(num_list)
        std = calc.stdDev(num_list, xbar)

        
        self.result_label.configure(text=f" \nThe mean is {xbar} \n The standard deviation is {std}")



    def close(self):
        self.root.destroy()    

    


calcGUI()












