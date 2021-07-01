class Car:
    #atribute of class
    car_count = 1

    #method
    def start(self, name, make, model):
        print('engine start up')
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    @staticmethod
    def get_class_details():
        print('this is class Car')

#first object
car_a = Car()
car_a.start('Corrola', 'Toyota', 2015)
print(car_a.name)
print(car_a.car_count)

#second object
car_b = Car()
car_b.start('City', 'Honda', 2013)
print(car_b.name)
print(car_b.car_count)

#staticmethod
Car.get_class_details()

#class Square
class Square:
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b
print(Square.get_squares(3, 5))

#class second Car
class Car:
    def start(self):
        print('engine is start up')
car_a = Car()
print(car_a)

#class Car with method __str__
class Car:
    def __str__(self):
        return 'Car class object'
    def start(self):
        print('engine is start up')
car_a = Car()
print(car_a)

#class Car with __init__
class Car:
    #atribute of class
    car_count = 0

    #create class' method
    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)
car_a = Car()
car_b = Car()
car_c = Car()

#local variable
class Car:
    message1 = 'engine is start up'

    def start(self):
        message2 = 'Car is start up'
        return message2
car_a = Car()
print(car_a.message1)

#public, private, protect

class Car:
    def __init__(self):
        print('engine public')
        self.name ='corolla'
        self.__make = 'toyota'
        self._model = '1999'
car_a = Car()
car_b = Car()
car_c = Car()
print(car_a.name)
#print(car_b.make)#
#print(car_c.model)#

#inheritance Vehicle
class Vehicle:
    def vehicle_method(self):
        print('its parent method from class Vehicle')

class Car(Vehicle):
    def car_method(self):
        print('This is methos from daughter')
car_a = Car()
car_a.vehicle_method() #call method from parent class

#Multiple inheritance
#create class Vehicle
class Vehicle:
    def vehicle_method(self):
        print('This is parent method Vehicle x2')

#create Class Car, inherited Vehicle
class Car(Vehicle):
    def car_method(self):
        print('this is a daughter from class \' Car')

#create class Cycle, inherited Vehicle
class Cycle(Vehicle):
    def cycleMethod(self):
        print('this is daughter from class Cycle')
car_a = Car()
car_a.vehicle_method() #call method parent class
car_b = Cycle()
car_b.vehicle_method() #call method parent class

#Parent class is inherited by two children
class Camera:
    def camera_method(self):
        print('this is parent method from class Camera')

class Radio:
    def radio_method(self):
        print('this is parent method from class Radio')

class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print('this is daughter method from CellPhone')
cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()


#Polymorphism
class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)
car_a = Car()
car_a.start(10)
car_a.start(10, 20)

#create class Vehicle
class Vehicle:
    def print_details(self):
        print('this is parent method from class Vehicle')

#create class is inherited Vehicle
class Car(Vehicle):
    def print_details(self):
        print('this is daughter class from Car')

#create class Cycle is inherited Vehicle:
class Cycle(Vehicle):
    def print_details(self):
        print('this is daughter class from Cycle')
car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()