#test
import random
print("Yu-Gi-Oh! -Dark Ray-")
print("")

class MUnit:
    def __init__(self, name, power = 1):
        self.name = name
        self.power = power

def Rolldie():
    return random.randrange(1, 20, 1)

card1 = MUnit("Warrior")
card2 = MUnit("Spellcaster")

print(card1.name,"[",card1.power,"]")
print(card2.name,"[",card2.power, "]")
print("")

if (card1.power + Rolldie()) > (card2.power + Rolldie()):
    print(card1.name, "wins!")
elif (card2.power + Rolldie()) > (card1.power + Rolldie()):
    print(card2.name, "wins!")
else:
    print ("Tie!")
