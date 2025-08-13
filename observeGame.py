#Here will be all the necessary variables
defending = False

name = input("Name your character").lower()
if name == "jeff":
    power = 3
    defence = 3
    maxHP = 10
elif name == 'howard' or name == 'hexman':
    power = 5
    defence = 0
    maxHP = 15
elif name == 'mort':
    power = 2
    defence = 4
    maxHP = 9
elif name == 'luigi':
    power = 1
    defence = 5
    maxHP = 16
elif name == 'ty' or name == 'tyron' or name == 'tyler' or name == 'tiger' or name == 'tyson' or name == 'ginger':
    power = 1
    defence = 1
    maxHP = 3
else:
    power = 2
    defence = 2
    maxHP = 10
level = 1
HP = maxHP
magic = 5
name = name.upper(0)

print(name + " has encountered a Goblin! It is " + name + "\'s turn")
gHP = 7
gAtk = 2
gDef = 1
gMer = 0
checked = False
while HP > 0 and gHP > 0 and gMer < 5:
    action = input("What would you like to do? \n Attack \n Supa Slam (1 Magic) \n Check \n Talk \n Defend").lower()
    if action == "attack":
        damage = int((power * 1.2) - gDef)
        print(name + " punches the Goblin with full force. The Goblin takes " + str(damage) + " damage.")
        gHP = gHP - damage
    elif action == 'supa slam' or action == 'super slam' or action == 'slam':
        if magic > 0:
            magic = magic - 1
            damage = int((power * 2) - gDef)
            print(name + " slams the Goblin DOWN to the ground! The Goblin takes " + str(damage) + " damage.")
            gHP = gHP - damage
        else:
            print(name + " tries to slam the Goblin, but doesn't have any magic to do so.")
    elif action == 'check':
        choose = input("Check Who? \n " + name + " \n The Goblin").lower()
        if choose == name:
            print(name + " checks themselves. " + name + " has " + str(power) + " attack, " + str(defence) + " defence, and " + str(HP) + " HP.")
        elif choose == 'the goblin' or choose == 'goblin':
            print(name + " checks the enemy.")
            if gHP >= 3:
                print("The Goblin: " + str(gAtk) + " Attack and " + str(gDef) + " Defence. Looking for his mother.")
                checked = True
            else:
                print("The Goblin: " + str(gAtk) + " Attack and " + str(gDef) + " Defence. Has some major scars.")
        else:
            print(choose + " isn't in combat currently.")
    elif action == 'talk':
        if checked == True:
            print(name + " tells the Goblin where their mother is. The Goblin looks pleased.")
            gMer = gMer + 5
        else:
            print(name + " talks to the Goblin. The Goblin looks more at ease.")
            gMer = gMer + 1
            gDef = gDef - 1
    elif action == 'defend':
        print(name + " defends. Their defence doubles this turn.")
        defending = True
    elif action == 'what' or action == 'why':
        print(name + " questions why they are here. The goblin looks confused and goes on guard.")
        gAtk = gAtk - 1
        gDef = gDef + 1
    else:
        print(name + " doesn't have the ability to do that.")
    
    if gHP <= 0:
        level = level + 1
        power = power + 1
        defence = defence + 1
        maxHP = maxHP + int(HP / 3)
        print("The Goblin falls over brutally injured. " + name + " won! You grew to Level " + str(level))
    elif gMer >= 5 and checked == True:
        print("The Goblin thanks you for telling them where their mother is. " + name + " won!")
    elif gMer >= 5 and checked == False:
        print("The Goblin deems " + name + " as a non-threat. The Goblin says they're sorry and takes off. " + name + " won!")
    else:
        if gMer >= 3:
            print("The Goblin conciders if what they are fighting for is really worth it.")
        else:
            damage = int((gAtk * 2) - defence - gMer)
            if damage > 0 and defending == False:
                print("The Goblin swings at full force. " + name + " takes " + str(damage) + " damage.")
                HP = HP - damage
            elif damage > 0 and defending == True:
                print("The Goblin swings at full force. " + name + " takes " + str(damage - 1) + " damage.")
                HP = HP + 1 - damage
            else:
                print("The Goblin swings at full force. " + name + " takes 1 damage.")
                HP = HP - 1

    if HP <= 0:
        print(name + " falls over, brutally injured. \n GAME OVER")


