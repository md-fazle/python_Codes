class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
     print("sail")

class Plane(Vehicle):
    def move(self):
        print("Fly!")
car1=Car("Ford","mustang")
boat1=Boat("Ibiza","Touring 20")
Plane1=Plane("Boeing","747")

for x in (car1,boat1,Plane1):
    print(x.brand)
    print(x.model)
    x.move()