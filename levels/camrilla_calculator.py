import camrilla
from tkinter import *

class MyButton:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.high = Label(frame, text = "High: ")
        self.high.grid(row = 2, column = 0)

        self.high_text = Entry(frame)
        self.high_text.grid(row = 2, column = 2)

        self.low = Label(frame, text="Low: ")
        self.low.grid(row=3, column=0)

        self.low_text = Entry(frame)
        self.low_text.grid(row=3, column=2)

        self.close = Label(frame, text="Close: ")
        self.close.grid(row=4, column=0)

        self.close_text = Entry(frame)
        self.close_text.grid(row=4, column=2)

        self.submit_button = Button(frame, text="Calculate", command = self.camrilla_calculate)
        self.submit_button.grid(row=5,column=2)

        self.r1_label = Label(frame, text="R1: ")
        self.r1_label.grid(row = 6)

        self.r2_label = Label(frame, text="R2: ")
        self.r2_label.grid(row=7)

        self.r3_label = Label(frame, text="R3: ")
        self.r3_label.grid(row=8)

        self.r4_label = Label(frame, text="R4: ")
        self.r4_label.grid(row=9)

        self.r5_label = Label(frame, text="R5: ")
        self.r5_label.grid(row=10)

        self.s1_label = Label(frame, text="S1: ")
        self.s1_label.grid(row=11)

        self.s2_label = Label(frame, text="S2: ")
        self.s2_label.grid(row=12)

        self.s3_label = Label(frame, text="S3: ")
        self.s3_label.grid(row=13)

        self.s4_label = Label(frame, text="S4: ")
        self.s4_label.grid(row=14)

        self.s5_label = Label(frame, text="S5: ")
        self.s5_label.grid(row=15)
        
    
    def camrilla_calculate(self):
        high = float(self.high_text.get())
        low = float(self.low_text.get())
        close = float(self.close_text.get())

        c = camrilla.Camrilla(high, low, close)

        text = self.r1_label.cget("text") + str(c.r1())
        self.r1_label.configure(text=text)

        text = self.r2_label.cget("text") + str(c.r2())
        self.r2_label.configure(text=text)

        text = self.r3_label.cget("text") + str(c.r3())
        self.r3_label.configure(text=text)

        text = self.r4_label.cget("text") + str(c.r4())
        self.r4_label.configure(text=text)

        text = self.r5_label.cget("text") + str(c.r5())
        self.r5_label.configure(text=text)

        text = self.s1_label.cget("text") + str(c.s1())
        self.s1_label.configure(text=text)

        text = self.s2_label.cget("text") + str(c.s2())
        self.s2_label.configure(text=text)

        text = self.s3_label.cget("text") + str(c.s3())
        self.s3_label.configure(text=text)

        text = self.s4_label.cget("text") + str(c.s4())
        self.s4_label.configure(text=text)

        text = self.s5_label.cget("text") + str(c.s5())
        self.s5_label.configure(text=text)
        

calculator = Tk()
b = MyButton(calculator)
calculator.mainloop()
