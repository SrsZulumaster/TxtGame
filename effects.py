import json

import pandas as pd
'''
Currently a testing file to try implementations before applying them to real code

'''
with open("is_explored.json", "w+") as file:
    dicty = {"explore" : [[0,0],[1,0]]}
    json.dump(dicty, file, indent=4)


