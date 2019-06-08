import random

# Define the soldier class


class Soldier:
    # The soldiers_count is a class variable. It does not relate to objects.
    soldiers_count = 0

    # This intializer function is called the moment we create an object.
    # Here we are passing 3 parameters: name, weaponDamage and HP
    # These parameters are then assigned to object variables or
    # attributes of the object being created
    def __init__(self, name, weaponDamage, HP):
        self.name = name
        self.damage = weaponDamage
        self.hp = HP
        Soldier.soldiers_count += 1

    # The attack function takes one parameter called 'otherSoldier'
    # in order to access its information
    # In this case, we want to reduce the HP of the other soldier
    def attack(self, otherSoldier):
        otherSoldier.hp = otherSoldier.hp - self.damage
        print(f"{self.name} attacked {otherSoldier.name}" +
              f" with {self.damage} damage")

    # This function prints the HP of the soldier.
    # However, if he is dead, it will print that he is dead
    def status(self):
        if self.hp <= 0:
            print(f"{self.name} is dead")
        else:
            print(f"{self.name} has {self.hp} HP")

    # The purpose of this special function is to make the object printable
    # In other words, when it gets passed inside a print() it shows something
    def __str__(self):
        return f"{self.name} has {self.damage} damage and {self.hp} HP"


# This is a Sniper class inherited from the Soldier class
# Which means all the attributes and functions of the Soldier class
# will be inherited to Sniper class
class Sniper(Soldier):
    def __init__(self, name, weaponDamage, HP, accuracy):
        # The below line uses the super() function to call
        # the initializer of the parent class
        # Note that the __init__ function of the parent class takes 3 arguments
        super().__init__(name, weaponDamage, HP)
        self.accuracy = accuracy

    # Here we are re-defining the attack() function. This is called (override)
    def attack(self, otherSoldier):
        # This is a function under the 'random' module called 'choices'
        # It takes a list of options along with
        # a list of probabilities for these options
        # It returns a list with the randomly selected option
        shotType = random.choices(["headShot", "notHeadShot"], [
                                  self.accuracy, 1 - self.accuracy])[0]

        # If the shotType is headShot, then the otherSoldier immediately dies
        if shotType == "headShot":
            print(f"{self.name} attacked with headshot")
            otherSoldier.hp = 0
        else:
            # If the shotType is notHeadShot, then we attack normally
            # We can do this by calling the attack function of the parent class
            super().attack(otherSoldier)


# Define two soldiers
s1 = Soldier("Fahd", 10, 100)
sniper1 = Sniper("Osamah", 20, 30, 0.3)

# Print the soldiers status
print(f"Player 1: {s1}")
print(f"PLayer 2: {sniper1}")

# Make the two soldiers fight in turns
round = 1
turn = -1

while s1.hp > 0 and sniper1.hp > 0:
    print("\n======================")
    print(f"Round {round}")

    # This is a way to make sure the user selects a valid option
    # Study this carefully, you will use it two times in the second project
    while turn not in [1, 2]:
        turn = int(input("Enter the player number to make him attack: "))

    if turn == 1:
        # Note here s1 is attacking sniper1
        # We are passing sniper1 as an argument
        # because we want to decrease his HP
        s1.attack(sniper1)
        turn = 2
    else:
        sniper1.attack(s1)
        turn = 1

    round += 1
    # Print players status
    s1.status()
    sniper1.status()
    # Reset the turn
    turn = -1


print("\n==================\nGAME OVER")
# print the winner
if s1.hp > 0:
    print(f"{s1.name} is the WINNER!!")
else:
    print(f"{sniper1.name} is the WINNER!!")
