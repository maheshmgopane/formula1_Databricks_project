class Character:# This is a class definition for a character in a game. It has attributes for name, health, and attack power, and a method to perform an attack.
    def __init__(self, name, health, attack,blood):# This is the constructor method that initializes the attributes of the Character class when an instance is created. It takes three parameters: name, health, and attack, and assigns them to the instance variables self.name, self.health, and self.attack respectively.
        self.name = name # This assigns the value of the name parameter to the instance variable self.name, which can be accessed by other methods in the class.
        self.health = health # This assigns the value of the health parameter to the instance variable self.health, which can be used to track the character's health status in the game.
        self.attack= attack # This assigns the value of the attack parameter to the instance variable self.attack, which represents the character's attack power in the game.
        self.blood= blood # This initializes an additional attribute called self.blood to the value of the blood parameter, which could represent the character's blood level or a similar attribute in the game.
    def attack_enemy(self):# This is a method that simulates an attack action performed by the character. When called, it prints a message indicating the character's name and the amount of damage they are dealing based on their attack attribute.
        print(f"{self.name} attacks with {self.attack} damage and has {self.blood} blood!")# This line uses an f-string to format the output message, including the character's name and attack damage.
warrior = Character("Thor", 100, 20, 'red')# This creates an instance of the Character class named warrior, with the name "Thor", health of 100, and attack power of 20.
mage = Character("Gandalf", 80, 25, "White")# This creates another instance of the Character class named mage, with the name "Gandalf", health of 80, and attack power of 25.
archer= Character("Legolas", 90, 15, 'green')# This creates a third instance of the Character class named archer, with the name "Legolas", health of 90, and attack power of 15. 
warrior.attack_enemy()# This calls the attack_enemy method on the warrior instance, which will print "Thor attacks with 20 damage!" to the console.
mage.attack_enemy()#   This calls the attack_enemy method on the mage instance, which will print "Gandalf attacks with 25 damage!" to the console.
archer.attack_enemy()# This calls the attack_enemy method on the archer instance, which will print "Legolas attacks with 15 damage!" to the console.

