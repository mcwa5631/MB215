class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self): #public info
        print(f"car details: {self.year} {self.make} {self.model}")

    def __update_model(self, new_model):
        self.model = new_model #updates cars model
        print(f"Model updated to: {self.model}")

    def update_model_publicly(self, new_model):
        self.__update_model(new_model) #calls updated private model


if __name__ == "__main__":
    my_car = Car("Hyundai", "SanteFe", 2012) #creates car attributes 

    my_car.display_info()  # outputs car public info

    my_car.update_model_publicly("kona")  #model updates to kona

#Display updated car details
    my_car.display_info()