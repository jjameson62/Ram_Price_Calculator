import tkinter as tk #import the tkinter module with the alias tk in our script
#import pricing
import math as m # imports the math module with the alias m
root=tk.Tk() # initalizes the main application window, refered to as root
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
root.title('Ram Calculator') # main window (root) title is set to 'Circle Circumference Calculator'
ddr=4 # default ddr version
from ram import calculate_price as RamCalculator

calculator = RamCalculator()


def set_ddr(number):
    global ddr
    ddr=number
#Calculate the price
def calculate_price():
    try:
        year = int(year_LabelValue.get())
        gb = int(gb_LabelValue.get())
        speed = int(speed_LabelValue.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for all fields")
        return

    if year < 2007 or year > 2026:
        messagebox.showerror("Error", "Please enter a Year (2007-2026)") # displays a error message to user
        year_LabelValue.set("")
        gb_LabelValue.set("")
        speed_LabelValue.set("")
        return

    if ddr == 4 and year < 2014:
        messagebox.showerror("Error", "DDR4 was not released until 2014!!1") # displays a error message to user
        year_LabelValue.set("")
        gb_LabelValue.set("")
        speed_LabelValue.set("")
        return

    if ddr == 5 and year < 2020:
        messagebox.showerror("Error", "DDR5 was not released until 2020!!!") # displays a error message to user
        year_LabelValue.set("")
        gb_LabelValue.set("")
        speed_LabelValue.set("")
        return

    total = calculator.total_price(
        ddr=f"DDR{ddr}",
        speed=speed,
        gb=gb,
        year=year,
    )
    messagebox.showinfo("Price", f"Total price: ${total}")
       
title_Label = tk.Label(root,text = 'Ram Calculator') #Title side label text
title_Label.grid(row=0, column=1) #grid position of title on screen

#Year input
year_Label = tk.Label(root,text = 'Enter The Year (2007-2026):') #'first number' side label text
year_Label.grid(row=3, column=0) #grid position of first_label on screen
year_LabelValue=tk.StringVar() #variable to string value for input
year_LabelEntry=tk.Entry(root,width=25,textvariable=year_LabelValue) # a side text entry attributes
year_LabelEntry.grid(row=3,column=1) # 'A' side text entry label grid position

#GB input
gb_Label = tk.Label(root,text = 'Enter the GB:') #'first number' side label text
gb_Label.grid(row=4, column=0) #grid position of first_label on screen
gb_LabelValue=tk.StringVar() #variable to string value for input
gb_LabelEntry=tk.Entry(root,width=25,textvariable=gb_LabelValue) # a side text entry attributes
gb_LabelEntry.grid(row=4,column=1) # 'A' side text entry label grid position


#Ram speed
speed_Label = tk.Label(root,text = 'Enter the RAM speed:') #'first number' side label text
speed_Label.grid(row=5, column=0) #grid position of first_label on screen
speed_LabelValue=tk.StringVar() #variable to string value for input
speed_LabelEntry=tk.Entry(root,width=25,textvariable=speed_LabelValue) # a side text entry attributes
speed_LabelEntry.grid(row=5,column=1) # 'A' side text entry label grid position

#DDR version 
gb_Label = tk.Label(root,text = 'Select DDR version:') #'first number' side label text
gb_Label.grid(row=6, column=0) #grid position of first_label on screen

#Button anchor <--- Used Copilot
ddr_frame = tk.Frame(root)
ddr_frame.grid(row=6, column=1, sticky="ew")
for column in range(3):
    ddr_frame.columnconfigure(column, weight=1, uniform="ddr")

#DDR3 button
ddr3_btn=tk.Button(ddr_frame,text="DDR3",command=lambda:set_ddr(3))
ddr3_btn.grid(row=0,column=0, padx=(0, 4), sticky="ew")

#DDR4 button
ddr4_btn=tk.Button(ddr_frame,text="DDR4",command=lambda:set_ddr(4))
ddr4_btn.grid(row=0,column=1, padx=(0, 4), sticky="ew")
#DDR5 button 
ddr5_btn=tk.Button(ddr_frame,text="DDR5",command=lambda:set_ddr(5))
ddr5_btn.grid(row=0,column=2, sticky="ew")

#Calculate the price
calculate_btn=tk.Button(root,text="Calculate Price",command=lambda:calculate_price())
calculate_btn.grid(row=10,column=1)



#Exit button
exitButton = tk.Button(root,text='Exit',command=root.destroy) #exit button
exitButton.grid(row=10,column=0) #exit button grid


#formatting the different text feilds and labels
for child in root.winfo_children(): #for a every child in the window
    child.grid_configure(padx=10,pady=7) #apply padding to the child



root.mainloop()
