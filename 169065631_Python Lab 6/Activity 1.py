# car.py
class Car:
    def __init__(self, make, model, year):
        self.make = make #initializes attributes
        self.model = model
        self.year = year
        pass

    def __str__(self):
        # returns a string of the car attributes 
        return f"{self.year} {self.make} {self.model}"

# Example usage
if __name__ == "__main__":
    my_car = Car("Hyndyai", "Sante Fe", 2015) #sets the attributes for class
    print(my_car)  # outputs attributes set under class