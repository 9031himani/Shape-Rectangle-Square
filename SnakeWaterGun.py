import random


def game_win(comp, you):
     if comp==you:
          return None

     elif comp=='s':
          if you=='w':
               return False
          elif you=='g':
               return False

     elif comp=='w':
          if you=='g':
               return False
          elif you=='s':
               return True

     elif comp=='g':
          if you=='s':
               return False
          elif you=='w':
               return True


print("comp turn : Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
     comp = "s"
elif randNo == 2:
     comp = 'w'
elif randNo == 3:
     comp = 'g'


you = input("Your turn : Snake(s) Water(w) Gun(g)?")
a = game_win(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
     print("The game is a tie")
elif a:
     print("you win")
else:
     print("you lose")
