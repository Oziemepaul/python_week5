# week5.py
class Superhero:
    def _init_(self, name, alter_ego, superpower, health):
        self.name = name  # The superhero's official name
        self.alter_ego = alter_ego  # The hero's secret identity
        self.superpower = superpower  # Their unique ability
        self.health = health  # A numerical value for health
        self.is_active = True  # A boolean attribute

    def show_stats(self):
        """Displays the superhero's attributes."""
        print(f"Hero Name: {self.name}")
        print(f"Secret Identity: {self.alter_ego}")
        print(f"Superpower: {self.superpower}")
        print(f"Health: {self.health}")
        print(f"Status: {'Active' if self.is_active else 'Retired'}")

    def use_power(self):
        """Simulates the hero using their superpower."""
        print(f"{self.name} is using their power of {self.superpower}!")

class Sidekick(Superhero):
    """
    A class for a sidekick, which inherits from the Superhero class.
    """

    def _init_(self, name, alter_ego, superpower, health, team_leader):
        # Call the parent class constructor to inherit its attributes.
        super()._init_(name, alter_ego, superpower, health)
        self.team_leader = team_leader  # A new, unique attribute for the Sidekick class

    # Demonstrate Polymorphism by overriding a method.
    def use_power(self):
        """
        Overrides the parent method to show a different message.
        """
        print(f"{self.name} is assisting {self.team_leader} with their power of {self.superpower}!")
    
    # A new method specific to the Sidekick class.
    def support_leader(self):
        """A specific action for the sidekick."""
        print(f"{self.name} is providing support to {self.team_leader}.")

# Create an instance of the superhero class.
hero1 = Superhero("Captain Python", "Jack Devlin", "Code Manipulation", 100)
print("--- Superhero created ---")
hero1.show_stats()
hero1.use_power()
print("\n")

# Create an instance of the sidekick class.
sidekick1 = Sidekick("The Byte", "Sarah Coder", "Data Compression", 75, "Captain Python")
print("--- Sidekick created ---")
sidekick1.show_stats()
sidekick1.use_power()  # This calls the overridden method (Polymorphism)
sidekick1.support_leader()

# Activity 2
class Vehicle:
    """A generic class for a vehicle."""
    def move(self):
        """A method to represent movement."""
        print("This vehicle moves.")

class Car(Vehicle):
    """A class for a car, inheriting from Vehicle."""
    def move(self):
        """Overrides the move() method for a car."""
        print("Driving 🚗")

class Plane(Vehicle):
    """A class for a plane, inheriting from Vehicle."""
    def move(self):
        """Overrides the move() method for a plane."""
        print("Flying ✈")

# Create instances of each class
my_car = Car()
my_plane = Plane()
my_vehicle = Vehicle()

# Create a list of the objects
vehicles = [my_car, my_plane, my_vehicle]

# Iterate through the list and call the move() method on each object.
# The program automatically knows which move() method to call.
for vehicle in vehicles:
    vehicle.move()