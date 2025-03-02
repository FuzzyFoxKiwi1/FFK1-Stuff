import random

# Define classes and functions for the game

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.health = 100
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.skills = self.set_skills()

    def set_skills(self):
        skills = {
            "warrior": ["slash", "block"],
            "mage": ["fireball", "teleport"],
            "rogue": ["stealth", "backstab"]
        }
        return skills[self.char_class]

    def display_status(self):
        print(f"{self.name} the {self.char_class.capitalize()}")
        print(f"Level: {self.level}, Health: {self.health}, Experience: {self.experience}")
        print(f"Skills: {', '.join(self.skills)}")

    def level_up(self):
        self.level += 1
        self.health += 10
        self.experience = 0
        self.skills.append(random.choice(["power strike", "magic shield", "swift strike"]))
        print(f"{self.name} leveled up to level {self.level}!")

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")

class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward

    def display(self):
        print(f"Quest: {self.name}")
        print(f"Description: {self.description}")
        print(f"Reward: {self.reward}")

class Game:
    def __init__(self):
        self.player = None
        self.level = 1
        self.quests = []

    def start_game(self):
        self.intro()
        self.create_character()
        self.create_quests()
        while self.player.health > 0:
            self.display_menu()
        print("Game over!")

    def intro(self):
        print("Welcome to the Advanced Dungeon Adventure!")
        print("Embark on a journey through perilous dungeons, fight enemies, find treasures, and level up!\n")

    def create_character(self):
        name = input("Enter your character's name: ")
        print("Select your character class:")
        classes = ["warrior", "mage", "rogue"]
        for i, cls in enumerate(classes):
            print(f"{i + 1}: {cls.capitalize()}")
        choice = int(input("Enter the number of your class choice: "))
        char_class = classes[choice - 1]
        self.player = Character(name, char_class)
        print(f"\nWelcome, {name} the {char_class.capitalize()}!\n")

    def create_quests(self):
        self.quests.append(Quest("Defeat the Goblin King", "Defeat the Goblin King in the Dark Forest.", "100 gold"))
        self.quests.append(Quest("Retrieve the Ancient Artifact", "Find and retrieve the Ancient Artifact from the Ruins.", "200 gold"))

    def display_menu(self):
        print("1: Move forward")
        print("2: Look for treasures")
        print("3: Fight an enemy")
        print("4: Rest")
        print("5: View inventory")
        print("6: Use skill")
        print("7: Level up character")
        print("8: View quests")
        choice = input("Enter the number of your choice: ")
        self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == '1':
            self.move_forward()
        elif choice == '2':
            self.find_treasure()
        elif choice == '3':
            self.fight_enemy()
        elif choice == '4':
            self.rest()
        elif choice == '5':
            self.view_inventory()
        elif choice == '6':
            self.use_skill()
        elif choice == '7':
            self.level_up()
        elif choice == '8':
            self.view_quests()
        else:
            print("Invalid choice. Please try again.\n")

    def move_forward(self):
        print("You move deeper into the dungeon...\n")

    def find_treasure(self):
        treasures = ["gold coins", "a shiny gem", "an ancient artifact", "a health potion", "a sword", "a shield", "a bow", "arrows", "a magic staff"]
        treasure = random.choice(treasures)
        print(f"You found {treasure}!\n")
        self.player.inventory.append(treasure)

    def fight_enemy(self):
        enemies = [
            Enemy("Goblin", 30, 5),
            Enemy("Skeleton", 40, 6),
            Enemy("Giant Spider", 50, 8),
            Enemy("Dark Wizard", 70, 10)
        ]
        enemy = random.choice(enemies)
        print(f"You encountered a {enemy.name}!")
        while enemy.health > 0 and self.player.health > 0:
            action = input("Do you want to (1) attack or (2) use a skill? ")
            if action == '1':
                self.player_attack(enemy)
            elif action == '2':
                self.use_skill()
            enemy.attack(self.player)
            if self.player.health <= 0:
                print("You have been defeated!\n")
                return
        print(f"You defeated the {enemy.name}!\n")

    def player_attack(self, enemy):
        damage = random.randint(5, 15)
        enemy.health -= damage
        print(f"You attack the {enemy.name} for {damage} damage!")

    def rest(self):
        print("You take a moment to rest and regain your strength.\n")
        self.player.health += 20

    def view_inventory(self):
        print("Your inventory:")
        if self.player.inventory:
            for item in self.player.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
        print("\n")

    def use_skill(self):
        skills = self.player.skills
        skill = random.choice(skills)
        print(f"You used your {skill} skill!")
        # Add skill mechanics here
        print("Skill mechanics go here...\n")

    def level_up(self):
        if self.player.experience >= self.player.level * 100:
            self.player.level_up()
        else:
            print("Not enough experience to level up.\n")

    def view_quests(self):
        print("Current Quests:")
        for quest in self.quests:
            quest.display()
        print("\n")

game = Game()
game.start_game()
