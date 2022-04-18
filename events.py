from random import randrange
import pandas as pd


def fight(enemy, player):
    while enemy.health > 0:
        if player.health > 0:
            player_action = input("Would you like to attack or block?")

            if player_action == "attack":
                player.health -= enemy.attack
                enemy.health -= player.attack
                print(f'Your health is {player.health}')
                print(f'The enemy health is {enemy.health}')

            elif player_action == "block":

                if randrange(1, 7) > 4:
                    print("you managed to block the attack")
                    print(f'Your health is {player.health}')
                    print(f'The enemy health is {enemy.health}')

                else:
                    print("you failed to block")
                    print(f'Your health is {player.health}')
                    print(f'The enemy health is {enemy.health}')
                    player.health -= enemy.attack
        elif player.health <= 0:
            print("GAME OVER")
            break
    return player.health


# A function that generates an item for the player to find
# Earlier implementation relied on an item list and a dictionary
def item_pickup(player):
    weapon_df = pd.read_csv("Player_info/weapon_info.csv")
    pick_up_resolved = False
    weapon = weapon_df.player_weapon[randrange(0, 5)]
    weapon_damage = weapon_df.attack[weapon_df['player_weapon'] == weapon].item()
    while not pick_up_resolved:

        print(f"you found an item ({weapon}) the damage is {weapon_damage}")
        print(f'Your attack is {player.attack}')
        print("would you like to pick it up?")
        player_input = input()

        if player_input == "yes":
            player.weapon = weapon
            player.attack = weapon_damage
            pick_up_resolved = True

        elif player_input == "no":
            pick_up_resolved = True

        else:
            pick_up_resolved = False



