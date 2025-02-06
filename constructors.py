# constructor

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = Car("mustang", 2020, "red", False)
car2 = Car("bmw", 2020, "red", True)

print(car2.color)
print(car1.model)


"""
# if we create a main file and a car file we have to write car class in car file and import that to main file

in car.py -> 
            class Car:
                def __init__(self, model, year, color, for_sale):
                    self.model = model
                    self.year = year
                    self.color = color
                    self.for_sale = for_sale

other code in main.py ->

                    from car import Car     

                    car1 = Car("mustang", 2020, "red", False)
                    car2 = Car("bmw", 2020, "red", True)

                    print(car2.color)
                    print(car1.model)    

"""
