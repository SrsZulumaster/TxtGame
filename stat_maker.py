import pandas as pd
from Player_class import Player, Enemy
import json

# takes input from weapon_info.csv and player_stats.csv and generates a player
def player_character(i):
    player_df = pd.read_csv("Player_info/Player_stats.csv")
    weapon_df = pd.read_csv("Player_info/weapon_info.csv")
    name = player_df.name[i]
    weapon = player_df.weapon[i]
    health = player_df.health[i]
    location = [player_df.current_X[i], player_df.current_Y[i]]
    attack = weapon_df.attack[weapon_df["player_weapon"] == weapon].item()
    return Player(name, weapon, health, attack, location)


# Takes input from enemy_stats.csv and generates an enemy
def enemy_character(i):
    enemy_df = pd.read_csv("Player_info/enemy_stats.csv")
    name = enemy_df.name[i]
    attack = enemy_df.attack[i]
    health = enemy_df.health[i]
    weapon = enemy_df.weapon[i]
    enemy = Enemy(name, weapon, health, attack)
    return enemy


def insert_into_is_explored(i):
    explored = [i]
    dicty = {"is_explored": explored}
    with open("is_explored.json", "w+") as file:
        dicty = file
        json.dump(dicty, file, indent=4)
    print( dicty)


insert_into_is_explored([1,2,3,4])