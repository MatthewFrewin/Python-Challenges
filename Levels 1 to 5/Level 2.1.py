# Basic Character Class
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            print(f"{self.name}: Argh I'm Dead! Dead!!!")
            # Delete the character...
        else:
            print(f"Urgh! {self.name} took a hit of {amount} and now has {self.health} health remaining")

    # Bonus task: Add an attack(target) method that deals damage to another character
    def attach(self, target):
        target.take_damage(self.strength)


# Test
beholder = Character("Frank the Beholder", 30, 6)

beholder.take_damage(14)
beholder.take_damage(14)
beholder.take_damage(14)
