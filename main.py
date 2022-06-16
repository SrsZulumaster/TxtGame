from random import randrange
from Player_class import is_explored, mover
from events import fight, item_pickup
from stat_maker import player_character, enemy_character, insert_into_is_explored

'''
TO DO
player select
Text based game with DnD style mechanics.
Basic fighting implemented needs to be improved
Basic moving implemented needs to be improved
location tracking in file needs to be added (currently in a explored = [list])
Walls and next step sight needs adding
GRAPHICS aka a stretch goal

'''

i = 0  # player select number (To be implemented)
player = player_character(i)
insert_into_is_explored(player.location)
print(player.location)

while player.health > 0:
    player.location = mover(input("Where would you like to go? "), player.location)
    if is_explored(player.location):
        print("You have already been here")
    else:
        event_starter = randrange(1, 4)
        insert_into_is_explored(player.location)
        print(f'you rolled a {event_starter} at main.py line 30')
        if event_starter == 1:
            rand = randrange(0, 8)
            enemy = enemy_character(rand)
            print(f'You see a {enemy.name}, he has a {enemy.weapon} with'
                  f' {enemy.attack} attack and {enemy.health} health')
            fight(enemy, player)
        elif event_starter == 2:
            item_pickup(player)
        else:
            print("You find nothing")
            continue
