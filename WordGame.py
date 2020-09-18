import sys

print('''Welcome to the WordGame.
The game has been developed by Ishan Bhavsar.
Do give me suggestions at the end of the game.
Thank You.
''')

print("WELCOME TO THE PALACE.")
print("CHOOSE A CASKET:BLUE,ORANGE,RED OR GREEN.")
print('''This will lead you to some places.''')

input_1 = input('''Choose and type 1:
blue
green
orange 
red 
green 
 ''').upper()
if input_1 == "BLUE":
    print("You have entered a hospital.You can pick up a dog or a cat who will decide your future. ")
    input_2 = input("choose one: dog or cat. ").upper()
    if input_2 == "CAT":
        print("You are out of the large hospital.*A LARGE HOLE OPENS WHICH SUCKS YOU AND YOU REACH YOUR HOUSE.*")
        sys.exit()
    if input_2 == "DOG":
        print("You are stuck in the hospital now.")
        print('''You have a passage to your right and your left.
        Choose where you want to go.''')
        input_2_A = input("Left/Right ").upper()
        if input_2_A == "LEFT":
            print("You have reached a dead end.")
            print("You return to your original position.")
            print("You encountered a monster at that place which ate you for lunch.")
        if input_2_A == "RIGHT":
            print("*moving to the right*.You atlast reach a door which is heavy & is a bit open.Open it completely?")
            input_2_A1 = input("OPEN COMPLETELY?(YES/NO) ").upper()
            if input_2_A1 == "YES":
                print("Congratulations!You are now free")
                sys.exit()