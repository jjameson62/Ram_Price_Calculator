#initialize the variables and start the program
class calculate_price: #
    def base(self, ddr):
    prices = {
        "DDR3": 3.83,
        "DDR4": 7.81,
        "DDR5": 21.25,
    }
    return prices[ddr]
#classifies the price of increase for ram speed 
    def ram_speed(ddr, speed):
        ranges = {
    "DDR3": (1333, 1600),
    "DDR4": (2666, 3200),
    "DDR5": (5200, 6000),
        }
        low, high = ranges[ddr]

        if speed <= low:
            return 0.95
        elif speed <= high:
            return 1
        else:
            return 1.05
    def total_price(self, ddr, speed,)
        total_price = GB * base * 0.90 ** age

def validation(model, price, )
if model = and ddr3_bprice => 2007 
    print("Enter a year later than 2007 mus
   
    ddr4_byear = 2014


    ddr5_byear = 2020