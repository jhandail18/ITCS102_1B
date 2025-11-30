step = True
trial = 0

while step is True:
    dungeon = input("Would you like to walk into Dungeon?: (y/n) ")
    if dungeon == 'yes':
        print("You Entered to Dungeon")
        walk = input("Continue?: (y/n)")
        if walk == "y":
            trial += 1
            print("Walk deeper..")
            continue
        elif walk == 'n':
            print(f"You leaved the Dungeon.. You walked {trial} steps")
            break
        elif dungeon == 'n':
            print("Got scared and run away...")
            print(f"number of steps, {trial}")
            break
        
