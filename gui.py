import tkinter as tk #import the tkinter module with the alias tk in our script

root=tk.Tk() # initalizes the main application window, refered to as root
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
root.title('Ram Calculator') # main window (root) title is set to 'Circle Circumference Calculator'
ddr=4 # default ddr version
from ram import calculate_price as RamCalculator  # Import the pricing class and give it the local name RamCalculator

calculator = RamCalculator()  # Create the calculator object used to estimate RAM prices


def set_ddr(number):  # Define the function that remembers which DDR button was clicked
    global ddr  # Use the shared DDR selection rather than creating a local variable
    ddr=number  # Save the selected generation number for the next calculation

    #Button colored in <<< Copilot
    buttons = {3: ddr3_btn, 4: ddr4_btn, 5: ddr5_btn}

    for generation, button in buttons.items():
        selected = generation == ddr  # Check whether this button is selected
        background = "#2563eb" if selected else "#f0f0f0"
        foreground = "white" if selected else "black"

        button.config(
            bg=background,  # Set the background color
            fg=foreground,  # Set the text color
            activebackground=background,  # Keep the color while pressed
            activeforeground=foreground,
            relief="sunken" if selected else "raised",
        )

        #<<< Copilot

#Calculate the price
def calculate_price():  # Define what happens when the Calculate Price button is clicked
    try:  # Attempt to read the inputs so invalid number conversions can be caught
        year = int(year_LabelValue.get())  # Read the manufacturing year and convert its text to a whole number
        gb = int(gb_LabelValue.get())  # Read the capacity in GB and convert its text to a whole number
        speed = int(speed_LabelValue.get())  # Read the speed and convert its text to a whole number
    except ValueError:  # Handle a field that cannot be converted to a whole number
        messagebox.showerror("Error", "Please enter valid numbers for all fields")  # Tell the user that every input field needs a valid number
        return  # Stop this button callback without calculating a price
    
    total = calculator.total_price(  # Begin a call to the calculator and store its returned total
        ddr=f"DDR{ddr}",  # Convert the selected number, such as 4, to the dictionary key DDR4
        speed=speed,  # Pass the entered speed to the calculator speed parameter
        gb=gb,  # Pass the entered capacity to the calculator gb parameter
        year=year,  # Pass the entered manufacturing year to the calculator year parameter
    )
    total_price_per_gb = calculator.total_price_per_gb(
        ddr=f"DDR{ddr}",  # Convert the selected number, such as 4, to the dictionary key DDR4
        speed=speed,  # Pass the entered speed to the calculator speed parameter
        gb=gb,  # Pass the entered capacity to the calculator gb parameter
        year=year,  # Pass the entered manufacturing year to the calculator year parameter

    )  
    messagebox.showinfo("Price", f"Total price: ${total:.2f}\n" f"Price per GB: ${total_price_per_gb:.2f}",)  # Display the returned total price in a popup
       
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

#Button anchor <<< made by copilot
ddr_frame = tk.Frame(root)  # Create a container that keeps the three DDR buttons together
ddr_frame.grid(row=6, column=1, sticky="ew")  # Place the container under the input boxes and stretch it horizontally
for column in range(3):  # Visit each of the three button columns inside the container
    ddr_frame.columnconfigure(column, weight=1, uniform="ddr")  # Make this column share available space equally with the other button columns

#DDR3 button
ddr3_btn=tk.Button(ddr_frame,text="DDR3",command=lambda:set_ddr(3))  # Create a DDR3 button that saves 3 when clicked
ddr3_btn.grid(row=0,column=0, padx=(0, 4), sticky="ew")  # Place DDR3 first, stretch it horizontally, and leave a gap on its right

#DDR4 button
ddr4_btn=tk.Button(ddr_frame,text="DDR4",command=lambda:set_ddr(4))  # Create a DDR4 button that saves 4 when clicked
ddr4_btn.grid(row=0,column=1, padx=(0, 4), sticky="ew")  # Place DDR4 second, stretch it horizontally, and leave a gap on its right
#DDR5 button 
ddr5_btn=tk.Button(ddr_frame,text="DDR5",command=lambda:set_ddr(5))  # Create a DDR5 button that saves 5 when clicked
ddr5_btn.grid(row=0,column=2, sticky="ew")  # Place DDR5 third and stretch it horizontally

#Calculate the price
calculate_btn=tk.Button(root,text="Calculate Price",command=lambda:calculate_price())  # Create a button that runs the calculation callback when clicked
calculate_btn.grid(row=10,column=1)  # Place the Calculate Price button below the input boxes



#Exit button
exitButton = tk.Button(root,text='Exit',command=root.destroy) #exit button
exitButton.grid(row=10,column=0) #exit button grid


#formatting the different text feilds and labels
for child in root.winfo_children(): #for a every child in the window
    child.grid_configure(padx=10,pady=7) #apply padding to the child



root.mainloop()  # Keep processing window events and button clicks until the window closes
