class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model  #makes model attribute priavte by chnaging name
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.__model}") #displays car details publically

    def get_model(self):
        return self.__model #accesses private model 

    def set_model(self, new_model):
        # Public method to update the private model attribute
        self.__model = new_model
        print(f"Model updated to: {self.__model}")




if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2022)

    my_car.display_info()  #displays car details

    try:
        print(my_car.__model) #tries to access car model
    except AttributeError as e:
        print("error ", e)

    print("Current Model:", my_car.get_model())

    my_car.set_model("Camry")

    my_car.display_info()