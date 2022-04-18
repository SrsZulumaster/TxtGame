import pandas as pd
'''
Currently a testing file to try implementations before applying them to real code

'''
player_df = pd.read_csv("Player_info/Player_stats.csv")
weapon_df = pd.read_csv("Player_info/weapon_info.csv")

player_name = player_df.player_name[0]
player_weapons = player_df.weapon[0]
player_attack = weapon_df.attack[weapon_df["player_weapon"] == player_weapons].item()

print(player_name)
print(player_weapons)
print(player_attack)


