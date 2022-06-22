from Car import Car

class ElectricCar:

def __init__(self, trademark, model, year):
    super().__init__(trademark, model, year)
    self.battery_size = 75 # value in KWh

def describe_battery(self):
    print(f"This car has a {self.battery_size} KWh battery.")

def fill_gas_tank(self):
        print("This is an electric car, you don't need to fill the tank")



    my_tesla = ElectricCar('Tesla', '5', 2020)

    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    my_tesla.fill_gas_tank()

    print(my_tesla.tank)










