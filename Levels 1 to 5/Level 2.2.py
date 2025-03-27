import random

# Basic Character Class
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def get_name(self):
        return self.name

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            print(f"{self.get_name()}: Argh I'm Dead! Dead!!!")
            # Delete the character...
        else:
            print(f"Urgh! {self.get_name()} took a hit of {amount} and now has {self.health} health remaining")

    def attack(self, target):
        # 10% chance of a critical hit with double damage
        critical_hit = random.randint(1,10) == 1

        if critical_hit:
            print(f"Hells Bells! {self.get_name()} let out a battle cry and lands a whopper on {target.get_name()}.")
            target.take_damage(self.strength * 2)
        else:
            random_phrases = [
                f"{self.get_name()} says 'Have some of this!' and attacks {target.get_name()}.",
                f"{self.get_name()} whips their biscuit and tries to cause havoc for {target.get_name()}.",
                f"{self.get_name()} has fire in there belly and smashes into {target.get_name()}.",
                f"{self.get_name()} screams 'I'll teach you some manners!' and throws themself at {target.get_name()}."
            ]
            print(random.choice(random_phrases))
            target.take_damage(self.strength)

# Battle of the beasts...
beholder = Character("Frank the Beholder", 200, 6)
dragon = Character("Doris the Dragon", 120, 19)

turn = 1
while beholder.is_alive() and dragon.is_alive():
    print(f"Round {turn}:")
    beholder.attack(dragon)
    print()
    dragon.attack(beholder)
    print()
    turn += 1
    input("Press Enter key to continue...")


