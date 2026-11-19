import tkinter as tk #import the tkinter module with the alias tk in our script
import math as m # imports the math module with the alias m
root=tk.Tk() # initalizes the main application window, refered to as root
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
root.title('Ram Calculator') # main window (root) title is set to 'Circle Circumference Calculator'

title_Label = tk.Label(root,text = 'Ram Calculator') #Title side label text
title_Label.grid(row=0, column=0) #grid position of title on screen

year_Label = tk.Label(root,text = 'Enter The Year (from 2007):') #'first number' side label text
year_Label.grid(row=3, column=0) #grid position of first_label on screen
year_LabelValue=tk.StringVar() #variable to string value for input
year_LabelEntry=tk.Entry(root,width=25,textvariable=year_LabelValue) # a side text entry attributes
year_LabelEntry.grid(row=3,column=1) # 'A' side text entry label grid position

gb_Label = tk.Label(root,text = 'Enter The amount of GigaBytes:') #'first number' side label text
gb_Label.grid(row=4, column=0) #grid position of first_label on screen
gb_LabelValue=tk.StringVar() #variable to string value for input
gb_LabelEntry=tk.Entry(root,width=25,textvariable=gb_LabelValue) # a side text entry attributes
gb_LabelEntry.grid(row=4,column=1) # 'A' side text entry label grid position

gb_Label = tk.Label(root,text = 'Choose which DDR version') #'first number' side label text
gb_Label.grid(row=5, column=0) #grid position of first_label on screen


ddr3_btn=tk.Button(root,text="DDR3")
ddr3_btn.grid(row=5,column=1)

ddr4_btn=tk.Button(root,text="DDR4")
ddr4_btn.grid(row=5,column=2)

ddr4_btn=tk.Button(root,text="DDR5")
ddr4_btn.grid(row=5,column=3)


#formatting the different text feilds and labels
for child in root.winfo_children(): #for a every child in the window
    child.grid_configure(padx=10,pady=10) #apply padding to the child



root.mainloop()