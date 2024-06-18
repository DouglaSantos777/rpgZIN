from random import randint

lista_pokes = []

def criar_monstro():   
  level = randint(1 ,50)
  
  novo_poke = {
    "pokemon": f"Pokemon Inimigo {level}",
    "level": level,
    "dano": 5 * level,
    "hp": 90 + (10 * level)
  }
  
  lista_pokes.append(novo_poke)
  
  
def criar_varios_monstro():
    i = 100
    poke = 0
    while poke < i:
       criar_monstro()
       poke +=1

def mostra_pokes():
  for poke in lista_pokes:
    print(poke["pokemon"], poke["level"], poke["hp"], poke["dano"])

criar_varios_monstro()
mostra_pokes()


  