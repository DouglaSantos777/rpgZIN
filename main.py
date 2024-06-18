""" array = ["charmander", "bulbassauro", "squirtle" ]

print(end = "varivel aleatoria ")

dor i in array:
   print(i, end = "pikachu\n")
    
    
for i in ["cyndaquil", 2, "chikorita", "totodile", True, {"tipo: Fogo"}]:
   print(i)"""


pokes = [
    {"pokemon": "Charmander", "level": 1},
    {"pokemon": "Bulbassauro", "level": 1},
    {"pokemon": "Squirtle", "level": 1},
    {"pokemon": "Pikachu", "level": 1}   
]
    
    
#print(pokes[2]["pokemon"], pokes[2]['level'])


"""for poke in pokes:
    print(poke["pokemon"], poke["level"])"""
    
for poke in pokes:
    print(f"Pokemon : {poke['pokemon']} \nLevel: {poke['level']} " )
