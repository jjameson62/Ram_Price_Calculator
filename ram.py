#Estimate RAM prices using sample base prices and yearly depreciation at a rate of 10% per year
#The ram is deifned with their default "prices" the "released_year" and the "speed_range"
from tkinter import messagebox  #from the tkinter module, import ttk and messagebox functions alowing us to display and output text.
#Create a class to calculate the price
class calculate_price:

   # Refrence point for calculation
    current_year = 2026

    # Defines the starting price per GB
    prices = {
        "DDR3": 3.83, #3.83 $ in 2007  
        "DDR4": 7.81, #7.81 $ in 2016
        "DDR5": 21.25, #21.25 in 2020
    }
    #Sets the years the ram came out
    release_years = {
        "DDR3": 2007,
        "DDR4": 2014,
        "DDR5": 2020,
    }
    #gives ranges for the speed
    speed_ranges = {
        "DDR3": (1333, 1600),
        "DDR4": (2666, 3200),
        "DDR5": (5200, 6000),
    }
    # Verifies that ram also has a ddr version
    def base(self, ddr):
        if ddr not in self.prices:
            raise ValueError("\nChoose DDR3, DDR4, or DDR5.")
        return self.prices[ddr]

  
    #Validate the details before calculation
    def validate(self, ddr, speed, gb, year):
        self.ram_speed(ddr, speed)
        if gb <= 0:
            raise ValueError("\nCapacity must be a positive number of GB.")

        current_year = self.current_year
        first_year = self.release_years[ddr]
        if not first_year <= year <= current_year:
            raise ValueError(
                f"\nThe manufacturing year for {ddr} must be a whole number "
                f"between {first_year} and {current_year}."
            )
    #Define ram speed
    def ram_speed(self, ddr, speed):
        self.base(ddr)  # Check the generation before looking up its speed range.
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("\nRAM speed must be a positive number in MT/s.")

        low, high = self.speed_ranges[ddr]
        if speed < low or speed > high:
            raise ValueError(
                f"\nRAM speed must be a within correct range for {ddr}"
                f"\nLow: {low}"
                f"\nHigh: {high}"
            )

        
        if speed <= low:
            return 0.95
        elif speed <= high:
            return 1.0
        else:
            return 1.05    #Multipler for the value
        
    #Calculate the Price per GB after Depreciation
    def price_per_gb(self, ddr, speed, gb, year): 
        return self.total_price(ddr, speed, gb, year) / gb
    
    #Calculate the total price for the ram
    def total_price(self, ddr, speed, gb, year): 
        
        self.validate(ddr, speed, gb, year)
        age = self.current_year - year

        # Multiplying by 0.90 once per year keeps 90% of the previous value
        return round((gb * self.base(ddr) * self.ram_speed(ddr, speed) * 0.90 ** age),3)
    