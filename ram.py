#Estimate RAM prices using sample base prices and yearly depreciation at a rate of 10% per year
#The ram is deifned with their default "prices" the "released_year" and the "speed_range"
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
#Create a class to calculate the price
class calculate_price:  # Define a class that groups RAM price data, validation, and calculations

   # Refrence point for calculation
    current_year = 2026  
    # Defines starting price per GB
    prices = {  
        "DDR3": 3.83, #3.83 $ in 2007 
        "DDR4": 7.81, #7.81 $ in 2016 
        "DDR5": 21.25, #21.25 in 2020 
    } 
    #Sets the years the ram came out
    release_years = {  
        "DDR3": 2007,  # Set the earliest DDR3 manufacturing year to 2007
        "DDR4": 2014,  # Set the earliest DDR4 manufacturing year to 2014
        "DDR5": 2020,  # Set the earliest DDR5 manufacturing year to 2020
    } 
    #Gives ranges for the speed
    speed_ranges = {  
        "DDR3": (1333, 1600),  # Use 1333 and 1600 as the DDR3 speed thresholds
        "DDR4": (2666, 3200),  # Use 2666 and 3200 as the DDR4 speed thresholds
        "DDR5": (5200, 6000),  # Use 5200 and 6000 as the DDR5 speed thresholds
    }  
    #Verifies that ram also has a ddr version
    def base(self, ddr):  # Define a method that checks the DDR generation and returns its starting price
        if ddr not in self.prices:  # Check whether the requested generation is missing from the price table
            raise ValueError("Choose DDR3, DDR4, or DDR5.")  # Reject an unknown generation with an explanatory error
        return self.prices[ddr]  # Return the starting price per GB for the selected generation

  
    #Validate the details before calculation
    def validate(self, ddr, speed, gb, year):  # Define a method that checks the supplied RAM details before pricing
        self.ram_speed(ddr, speed)  # Check the generation and speed by calling the speed multiplier method
        if gb <= 0:  # Check whether the capacity is zero or negative
            raise ValueError("Capacity must be a positive number of GB.")  # Reject a capacity that is not greater than zero

        current_year = self.current_year  # Read the calculator reference year into a local variable
        first_year = self.release_years[ddr]  # Look up the earliest manufacturing year for the selected generation
        if not first_year <= year <= current_year:  # Check whether the supplied year falls outside the permitted range
            raise ValueError(  # Begin raising an error describing the permitted manufacturing years
                f"The manufacturing year for {ddr} must be a whole number "  # Include the selected generation in the error message
                f"between {first_year} and {current_year}."  # Include the first and last permitted years in the same error message
            ) 
        
    def ram_speed(self, ddr, speed):  # Define a method that validates speed and returns a price multiplier
        self.base(ddr)  # Check the generation before looking up its speed range.
        if not isinstance(speed, (int, float)) or speed <= 0:  # Check whether speed is not numeric or is zero or negative
            raise ValueError("RAM speed must be a positive number.")  # Reject a speed that is not a positive number
        #Assigns a + or - value based on speed
        low, high = self.speed_ranges[ddr]  # Read the low and high thresholds for the selected DDR generation
        if speed <= low:  # Check whether speed is at or below the low threshold
            return 0.95  # Return a multiplier that reduces the price by five percent
        elif speed <= high:  # Otherwise, check whether speed is at or below the high threshold
            return 1.0  # Return a multiplier that leaves the price unchanged
        else:  # Handle a speed above the high threshold
            return 1.05    #Multipler for the value
        
    #Calculate the Price per GB after Depreciation
    def total_price_per_gb(self, ddr, speed, gb, year):  # Define a method that calculates the estimated price for one GB
        return self.total_price(ddr, speed, gb, year) / gb  # Calculate the total price and divide it by the capacity in GB
    
    #Calculate the total price for the ram
    def total_price(self, ddr, speed, gb, year):  # Define a method that calculates the estimated total RAM price
        self.validate(ddr, speed, gb, year)  # Validate all supplied details before doing the price calculation
        age = self.current_year - year  # Subtract the manufacturing year from the reference year to find the age
        return round(gb * self.base(ddr) * self.ram_speed(ddr, speed) * 0.90 ** age, 2, ) #Calculate 10 percent depreciation while keeping 90 percent value every year
        
