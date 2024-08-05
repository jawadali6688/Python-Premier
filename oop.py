# class Car:
#     type = "Car" # Class Attribute
#     weight = "185KG"
#     def __init__(self, name):
#         self.name = name  # instance attribute --> additional information 
        
#     def show_details(self):
#         return f"Car Name is {self.name}"
# class PetrolCar:
    
#     def display_details(self):
#         return f"This is petrol car"

# class ElectricCar(Car):
#     def __init__(self, name, type):
#         self.type = type
#         super().__init__(name)
        

#     def get_details(self):
#         return f"Car name is {self.name} and it's type is {self.type}"
    
    
# class SimpleCar(PetrolCar, Car): #Multiple inheritance
#     pass    

    
# my_car = Car("Tesla") 

# my_car_2 = ElectricCar("New Tesla", "Electric")

# print(my_car.show_details())
# print(my_car.get_details())
# print(my_car_2.show_details())
# print(my_car_2.get_details())



# my_car_3 = SimpleCar("Mclearn")

# print(my_car_3.display_details())
# print(my_car_3.show_details())



# Polymorphism



class Car:
    type = "Car" # Class Attribute
    weight = "185KG"
    def __init__(self, name):
        self.name = name  # instance attribute --> additional information 
        
    def show_details(self):
        return f"This is Car"
class PetrolCar:
    
    def show_details(self):
        return f"This is petrol car"

class ElectricCar():
    def show_details(self):
        return f"This is electric car"
    
     


my_car1 = Car("Tesla")
my_car2 = ElectricCar()
my_car3 = PetrolCar()


print(my_car1.show_details())
print(my_car2.show_details())
print(my_car3.show_details())

