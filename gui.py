import tkinter as tk #import the tkinter module with the alias tk in our script
#import pricing
import math as m # imports the math module with the alias m
root=tk.Tk() # initalizes the main application window, refered to as root
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
root.title('Ram Calculator') # main window (root) title is set to 'Circle Circumference Calculator'
ddr_version=4 # default ddr version



def set_ddr_version(number):
    global ddr_version
    ddr_version=number

def calculate_price():
    year=int(year_LabelValue.get())
    amount_of_gigs=int(gb_LabelValue.get())
    if year < 2007 and year > 2026:
        messagebox.showerror("Error", "Please enter a Year (2007-2008)") # displays a error message to user
        year_LabelValue.set("")
        gb_LabelValue.set("")
        return
    
    if ddr_version == 4 and year < 2014:
       messagebox.showerror("Error", "DDR4 was not released till 2014!!!") # displays a error message to user
       year_LabelValue.set("")
       gb_LabelValue.set("")
       return

    if ddr_version == 5 and year < 2020:
       messagebox.showerror("Error", "DDR4 was not released till 2020!!!") # displays a error message to user
       year_LabelValue.set("")
       gb_LabelValue.set("")
       return
    


    




title_Label = tk.Label(root,text = 'Ram Calculator') #Title side label text
title_Label.grid(row=0, column=1) #grid position of title on screen

year_Label = tk.Label(root,text = 'Enter The Year (from/including 2007):') #'first number' side label text
year_Label.grid(row=3, column=0) #grid position of first_label on screen
year_LabelValue=tk.StringVar() #variable to string value for input
year_LabelEntry=tk.Entry(root,width=25,textvariable=year_LabelValue) # a side text entry attributes
year_LabelEntry.grid(row=3,column=1) # 'A' side text entry label grid position

gb_Label = tk.Label(root,text = 'Enter The amount of GigaBytes:') #'first number' side label text
gb_Label.grid(row=4, column=0) #grid position of first_label on screen
gb_LabelValue=tk.StringVar() #variable to string value for input
gb_LabelEntry=tk.Entry(root,width=25,textvariable=gb_LabelValue) # a side text entry attributes
gb_LabelEntry.grid(row=4,column=1) # 'A' side text entry label grid position

gb_Label = tk.Label(root,text = 'Choose which DDR version:') #'first number' side label text
gb_Label.grid(row=5, column=0) #grid position of first_label on screen


ddr3_btn=tk.Button(root,text="DDR3",command=lambda:set_ddr_version(3))
ddr3_btn.grid(row=5,column=1)

ddr4_btn=tk.Button(root,text="DDR4",command=lambda:set_ddr_version(4))
ddr4_btn.grid(row=6,column=1)

ddr4_btn=tk.Button(root,text="DDR5",command=lambda:set_ddr_version(5))
ddr4_btn.grid(row=7,column=1)

calculate_btn=tk.Button(root,text="Calculate Price",command=lambda:calculate_price())
calculate_btn.grid(row=10,column=0)

#button for exiting below
exitButton = tk.Button(root,text='Exit',command=root.destroy) #exit button
exitButton.grid(row=0,column=0) #exit button grid


#formatting the different text feilds and labels
for child in root.winfo_children(): #for a every child in the window
    child.grid_configure(padx=10,pady=7) #apply padding to the child



root.mainloop()