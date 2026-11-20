#initialize the variables and start the program
class calculate_price:
    def base():
ddr3_bprice = 11.85 #dollars per gb pulled from google
ddr4_bprice = 14.06
ddr5_bprice = 18.75
#classifies the price of increase for ram speed 
    def ram_speed(ddr, speed):
        ranges = {
            "DDR3": (800, 1600),
            "DDR4": (1600, 3200),
            "DDR5": (3200, 6000),
        }
        low, high = ranges[ddr]

        if speed <= low:
            return 0.95
        elif speed <= high:
            return 1
        else:
            return 1.05
        
                

    
def calculation(model, mhz, ram_capacity)

def validation(model, price, )
if model = and ddr3_bprice => 2007 
    print("Enter a year later than 2007 mus
   
    ddr4_byear = 2014


    ddr5_byear = 2020
