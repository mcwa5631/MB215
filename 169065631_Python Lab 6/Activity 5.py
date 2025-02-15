class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

def compare_car_years(car1, car2): #compares car years using if statements
    if car1.year < car2.year:
        return f"{car1} is older than {car2}."
    elif car1.year > car2.year:
        return f"{car1} is newer than {car2}."
    else:
        return f"{car1} and {car2} are from the same year."


if __name__ == "__main__": #creates two car classes
    car1 = Car("toyota", "corolla ", 2018)
    car2 = Car("honda", "civic", 2022)
    result = compare_car_years(car1, car2) #compares the two cars
    print(result)  #prints the result of which car is older/newer