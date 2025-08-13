doorbroken = False
plypos = 0
plydead = False
plychoke = 3
ouch = 1
brokenhand = False
inventory = ['Nothing']

dinodead = False

plyhealth = 10
plyatck = 5
plydefense = False
plycharge = False
dinohealth = 30
dinoatck = 2
dinodefense = False
dinocharge = False
dinoaction = 0

ventopen = False
tookstool = False

while doorbroken == False and plydead == False:
    
    ply = input("There is a door here. \n").lower()

    if ply == "look north":
        print("The same thing as usual.")

    elif ply == "look west":
        print("Nothing. A blank void.")

    elif ply == 'look east' and 'Stool' not in inventory:
        print("There is a small golden key lying on a stool.")

    elif ply == 'look east' and "Stool" in inventory:
        print("There is a small golden key lying on the floor.")

    elif ply == 'take key':
        print("Your hand passes through the key like it wasn't even there.")

    elif ply == 'eat key':
        print("You heard a loud crunch sound. You didn't bite down yet.")

    elif ply == 'check key' or ply == 'inspect key':
        print("The key is the same color as the floor.")

    elif ply == 'check inventory' or ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.')
        inventory.append('Stool')
        tookstool = True

    elif ply == 'look south':
        print("You aren't an owl, are you?")

    elif ply == 'open door':
        print("You jiggle the handle. The door is locked.")

    elif ply == 'check door':
        print("It's just a simple door. It looks fragile, though.")

    elif ply == 'eat door':
        print("You put your mouth on the door. The door is too big to be eaten in one sitting.")
    
    elif ply == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True

    elif ply == 'fight door':
        print("""You prep for battle against a door.
Your actions are:
ATTACK
DEFEND
CHARGE""")
        doorFight = input("What will you do? \n").lower()
        if doorFight == 'attack' or doorFight == 'kill':
            print("You attack the door with brute force. It instantly breaks down. \n There is only a brick wall beyond the frame.")
            doorbroken = True
        elif doorFight == 'defend':
            print("You defended. The door doesn't do anything. You stop fighting it.")
        elif doorFight == 'charge':
            print("You charged. The door doesn't do anything. Perhaps it's best you save your energy for something else.")
        else:
            print("You can't think of how to perform that on a door. You disengage in combat.")

    elif ply == 'kill door':
        print("You brutally attack the door until it's nothing but rubble. \nYour hand hurts, but there is now a brick wall where the door was.")
        doorbroken = True
        ouch += 1

    elif ply == 'go north':
        print('You bang your head against the door.')

    elif ply == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe that there is a unbroken door in front of you.')
    
    elif ply == 'quit':
        print('Game over. ')
        plydead = True
        
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 0 and plydead == False:
    ply = input("There is no longer a door here. \n").lower()

    if ply == "check door":
        print("Nothing but splinters.")

    elif ply == 'check wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'break wall' and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand hurts.')
        ouch += 1

    elif ply == 'break wall' and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand is now broken. You can\'t break anymore.')
        brokenhand = True

    elif ply == 'break wall' and brokenhand == True:
        print("You wish you could do that, moron.")

    elif ply == "look north":
        print("A brick wall standing in a doorframe. The surface ripples when you touch it.")

    elif ply == "look west":
        print("Nothing.")

    elif ply == "look east" and 'Stool' in inventory:
        print("There was a stool here.")

    elif ply == "look east" and 'Stool' not in inventory:
        print("There is a stool with nothing on it whatsoever.")

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.')
        inventory.append('Stool')
        tookstool = True

    elif ply == "look south":
        print("You aren't an owl, are you?")
    
    elif ply == 'open door':
        print("You can't open splinters.")

    elif ply == 'break door':
        print("It's already broken.")

    elif ply == 'quit':
        print('Game over.')
        plydead = True

    elif ply == 'go north':
        print('You pass through brick like water. You choked to death. This is the end.\nGame Over\n\n\n\n  or is it?')
        plypos = 1

    elif ply == 'go east':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go west':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go south':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe that the Brick Wall looks unnatrual.')
    
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 1 and plydead == False:

    ply = input("There is no               here. \n").lower().split()

    if plychoke == 0:
        print("You somehow managed to choke to death for a second time. There aren't third chances in this world. \n\nGame over.")
        plydead = True

    elif 'break' in ply and brokenhand == False and plychoke == 1:
        print("You tried. but you failed. You felt the last bit of air escape your lungs.")
        plychoke == 0

    elif 'break' in ply and brokenhand == False and plychoke != 1:
        print('You broke. You lost Nothing.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        plypos = 2
        plychoke = 3
        inventory.remove('Nothing')
    
    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif 'break' in ply and brokenhand == True:
        print('You wish you could.')
        plychoke -= 1

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You thought about breaking.')
        plychoke -= 1

    else:
        plychoke -= 1
        print('There isn\'t a way to do that. You feel your lungs lose air.')


while plypos == 2 and tookstool == False and plydead == False:
    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'break glass':
        print('You bash your fist against the glass. It rebounds into your own face. Now your hand AND face hurt. Good job.')

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == "check dinosaur":
        print("You go to check the dinosaur. It reacts. \nBATTLE START!")
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 3
        
    elif ply == 'look west':
        print("Big plastic dinosaur. It looks suprisingly life-like.")

    elif ply == 'look south':
        print("Fake grass.")

    elif ply == 'look east':
        print('A basic beige wall.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe a suspicous looking dinosaur')

    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 3 and plydead == False:

    ply = input(f"Your health is: {plyhealth}. PLASTIC DINO's health is {dinohealth}. What do you do?\n").lower()

    def dinomove():
        import random
        dinoaction = random.randint(1, 10)
            
        if dinoaction > 5:
            print(f"PLASTIC DINO bit you for {dinoatck}!")
            plyhealth = plyhealth - dinoatck
            dinoatck = 2
            dinocharge = False
                
        elif dinoaction < 5:
            print("PLASTIC DINO defended! It won't take damage next turn!")
            dinodefense = True
    
        elif dinoaction == 5 and dinocharge == False:
            print("PLASTIC DINO charged! Its next attack will do double damage!")
            dinocharge = True
            dinoatck = 4
    
        elif dinoaction == 5 and dinocharge == True:
            print("PLASTIC DINO tried to charge! But it already did.")
    
        else:
            print("This will only print if something went horribly wrong.")

    if ply == ('attack'):
        print(f'You attacked PLASTIC DINO for {plyatck} damage!')
        dinohealth = dinohealth - plyatck
        plyatck = 5
        plycharge = False
        dinomove()

    elif ply == ('attack') and dinodefense == True:
        print('You attacked PLASTIC DINO! But it defended.')
        plyatck = 5
        plycharge = False
        dinodefense = False
        dinomove()

    elif ply == ('defend'):
        print('You defended! You won\'t take damage this turn.')
        plyatck = 5
        dinodefense = False
        dinomove()

    elif ply == ('charge'):
        print('You charged! You will do double damage on your next attack!')
        plyatck = 10
        plycharge = True
        dinodefense = False
        dinomove()

    elif ply == ('charge') and plycharge == True:
        print('You tried to charge again! But nothing happened...')
        plyatck = 10
        plycharge = True
        dinodefense = False
        dinomove()

    else:
        print("That isn't an action you can do.")
    
    if plyhealth == 0:
        print("You died! Loser!")
        plydead = True
    
    if dinohealth == 0:
        dinodead = True
        print("You won!")
        plypos = 2

            
while plypos == 2 and tookstool == True and plydead == False:

    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'look west' and 'Crowbar' not in inventory:
        print("Big plastic dinosaur. A crowbar dangles from its mouth.")

    elif ply == 'look east':
        print('A basic beige wall.')
    
    elif ply == 'break glass':
        print('You bash your fist against the glass. It rebounds into your own face. Now your hand AND face hurt. Good job.')

    elif ply == "check dinosaur":
        print("A large chunk of plastic in the shape of a dinosaur.")

    elif ply == 'look west' and 'Crowbar' in inventory:
        print("Big plastic dinosaur. It looks fake.")

    elif ply == 'take crowbar':
        print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth. Crowbar was added to inventory.")
        inventory.append('Crowbar')
        inventory.remove('Stool')

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground")

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You thought about using the stool to get the crowbar.')

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == False:
        print("You pry open the vent with the crowbar. It's too small to climb inside, but there is a red brick inside.")
        ventopen = True

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == True:
        print("You close the vent just so you can open it. Again.")

    elif ply == 'open vent' and 'Crowbar' not in inventory:
        print('You try to pull open the vent with your bare hands. It dosen\'t work.')

    else:
        print("Your thoughts seem incomprehensible.")
