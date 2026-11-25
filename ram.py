#Estimate RAM prices using sample base prices and yearly depreciation at a rate of 10% per year
#The ram is deifned with their default "prices" the "released_year" and the "speed_range"

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
    def base(self, ddr_version):
        if ddr_version not in self.prices:
            raise ValueError("Choose DDR3, DDR4, or DDR5.")
        return self.prices[ddr_version]

  
    #Validate the details before calculation
    def validate(self, ddr_version, speed, gb, year):
        self.ram_speed(ddr_version, speed)
        if gb <= 0:
            raise ValueError("Capacity must be a positive number of GB.")

        current_year = self.current_year
        first_year = self.release_years[ddr_version]
        if not first_year <= year <= current_year:
            raise ValueError(
                f"The manufacturing year for {ddr_version} must be a whole number "
                f"between {first_year} and {current_year}."
            )
    #Define the ram speed
    def ram_speed(self, ddr_version, speed):
        self.base(ddr_version)  # Check the generation before looking up its speed range.
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("RAM speed must be a positive number in MT/s.")

        low, high = self.speed_ranges[ddr_version]
        if speed <= low:
            return 0.95
        elif speed <= high:
            return 1.0
        else:
            return 1.05    
        
    #Calculate the Price per GB after Depreciation
    def price_per_gb(self, ddr_version, speed, gb, year): 
        return self.total_price(ddr_version, speed, gb, year) / gb
    
    #Calculate the total price for the ram
    def total_price(self, ddr_version, speed, gb, year): 
        
        self.validate(ddr_version, speed, gb, year)
        age = self.current_year - year

        # Multiplying by 0.90 once per year keeps 90% of the previous value
        return gb * self.base(ddr_version) * self.ram_speed(ddr_version, speed) * 0.90 ** age
    
if __name__ == "__main__":
    # Run this file directly to try the calculations without opening the GUI.
    calculator = calculate_price()
    ddr_version, speed, gb, year = "DDR4", 3200, 16, 2020
    total = calculator.total_price(ddr_version, speed, gb, year)
    per_gb = calculator.price_per_gb(ddr_version, speed, gb, year)
    print(f"Default price per GB: ${calculator.base(ddr_version):.2f}")
    print(f"Estimated total price: ${total:.2f}")
    print(f"Estimated price per GB: ${per_gb:.2f}")
