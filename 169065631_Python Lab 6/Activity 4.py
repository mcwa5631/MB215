class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model  # Private attribute
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.__model}")

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model
        print(f"Model update: {self.__model}")

    def __str__(self): #string representation
        return f"{self.year} {self.make} {self.__model}"
    
if __name__ == "__main__":
    my_car = Car("toyota", "corolla", 2011)
    
    
    print(my_car)  # prints car using string method

    my_car.set_model("camry")  # updates trhe car model
    print(my_car) 