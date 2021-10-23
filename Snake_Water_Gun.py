import random

def Game_win(comp,you):
    if comp == you:
        return None
    elif comp =="s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp =="w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
print("Copm's turn: Snake(s) Water(w) Gun(g)")
randno = random.randint(1,3)

if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 2:
    comp = "g"

you = input("User's turn: Snake(s) Water(w) Gun(g)")
a = Game_win(comp,you)

print(f"comp choose {comp}")
print(f"user choose {you}")

if a == None:
    print("Tie the game")
elif a:
    print("You win")
else:
    print("You lose!")
