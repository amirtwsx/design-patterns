import copy

# Prototype Interface
class Prototype:
    def clone(self):
        pass

# Concrete Prototype
class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def show_details(self):
        return f"Car Model: {self.model}, Color: {self.color}"

# Client Code
car1 = Car("Sedan", "Red")
car2 = car1.clone()
car2.color = "Blue"  # Modify the clone's color

print(car1.show_details())  # Output: Car Model: Sedan, Color: Red
print(car2.show_details())  # Output: Car Model: Sedan, Color: Blue
