# Usually bool methods can be named is_alive for example
import json

import pandas as pd


# Checks if the character is alive
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True


# Checks which locations have been explored
# needs to be moved into a .csv file
def is_explored(location):
    with open("is_explored.json", "r") as file:
        explored = json.load(file)
    if location in explored:
        print(f'{explored} have been explored in player_class line 14')
        return True
    elif location not in explored:
        return False
    else:
        return print("an unexpected value in is_explored")


# Attributes shared between player and enemies
class SharedAttributes:
    def __init__(self, name: str, weapon: str, health: int, attack: int):
        self.name = name
        self.weapon = weapon
        self.attack = attack
        self.health = health
        self.isAlive = is_alive(self.health)


# moves the character dependent on direction
def mover(command, location):  # command = up , location = [0,0]
    if command == "up":  # true
        new_loc = [location[0] + 1, location[1]]  # location[0][0] + 1, location[0][1] == [[1, 0]]
        return new_loc
    elif command == "down":
        new_loc = [location[0] - 1, location[1]]  # location[0][0] + 1, location[0][1] == [[1, 0]]
        return new_loc
    elif command == "right":
        new_loc = [location[0], location[1] + 1]  # location[0][0] + 1, location[0][1] == [[1, 0]]
        return new_loc
    elif command == "left":
        new_loc = [location[0], location[1] - 1]  # location[0][0] + 1, location[0][1] == [[1, 0]]
        return new_loc


# two different classes with same attributes to expand on later
class Player(SharedAttributes):

    def __init__(self, name, weapon, health, attack, location):
        super().__init__(name, weapon, health, attack)
        self.location = location


class Enemy(SharedAttributes):
    def __init__(self, name, weapon, health, attack):
        super().__init__(name, weapon, health, attack)
