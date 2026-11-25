"""Estimate RAM prices using sample base prices and yearly depreciation."""

class calculate_price:
    """Keep the pricing calculations separate from the Tkinter interface."""

    # Update this value when the calendar year changes.
    current_year = 2026

    # These are your starting prices per GB, not live market prices.
    prices = {
        "DDR3": 3.83,
        "DDR4": 7.81,
        "DDR5": 21.25,
    }

    release_years = {
        "DDR3": 2007,
        "DDR4": 2014,
        "DDR5": 2020,
    }

    speed_ranges = {
        "DDR3": (1333, 1600),
        "DDR4": (2666, 3200),
        "DDR5": (5200, 6000),
    }

    def base(self, ddr):
        """Return the default price per GB for a DDR generation."""
        if ddr not in self.prices:
            raise ValueError("Choose DDR3, DDR4, or DDR5.")
        return self.prices[ddr]

    def ram_speed(self, ddr, speed):
        """Return the price multiplier for RAM speed in MT/s."""
        self.base(ddr)  # Check the generation before looking up its speed range.
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("RAM speed must be a positive number in MT/s.")

        low, high = self.speed_ranges[ddr]
        if speed <= low:
            return 0.95
        elif speed <= high:
            return 1.0
        else:
            return 1.05

    def validation(self, ddr, speed, gb, year):
        """Reject specifications that cannot describe valid RAM."""
        self.ram_speed(ddr, speed)
        if not isinstance(gb, (int, float)) or gb <= 0:
            raise ValueError("Capacity must be a positive number of GB.")

        current_year = self.current_year
        first_year = self.release_years[ddr]
        if not isinstance(year, int) or not first_year <= year <= current_year:
            raise ValueError(
                f"The manufacturing year for {ddr} must be a whole number "
                f"between {first_year} and {current_year}."
            )

    def total_price(self, ddr, speed, gb, year):
        """Estimate the total price from capacity, speed, and age."""
        self.validation(ddr, speed, gb, year)
        age = self.current_year - year

        # Multiplying by 0.90 once per year keeps 90% of the previous value.
        return gb * self.base(ddr) * self.ram_speed(ddr, speed) * 0.90 ** age

    def price_per_gb(self, ddr, speed, gb, year):
        """Return the estimated price per GB after speed and age adjustments."""
        return self.total_price(ddr, speed, gb, year) / gb


if __name__ == "__main__":
    # Run this file directly to try the calculations without opening the GUI.
    calculator = calculate_price()
    ddr, speed, gb, year = "DDR4", 3200, 16, 2020
    total = calculator.total_price(ddr, speed, gb, year)
    per_gb = calculator.price_per_gb(ddr, speed, gb, year)
    print(f"Default price per GB: ${calculator.base(ddr):.2f}")
    print(f"Estimated total price: ${total:.2f}")
    print(f"Estimated price per GB: ${per_gb:.2f}")
