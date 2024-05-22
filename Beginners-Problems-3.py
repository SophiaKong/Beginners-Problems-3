def check_height_for_rollercoaster():

    height = int(input("Enter your height in cm: "))
    
    if height >= 120:
        print("You can ride the rollercoaster!")
    else:
        print("Sorry. You can't ride the rollercoaster.")

check_height_for_rollercoaster()

treasure island ->
def treasure_island_adventure():
   
    print("You are exploring a rainforest in search of treasure.")
    print("Legend has it that there are some buried on a nearby island.")

    choice1 = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait): ").lower()

    if choice1 == "swim":
        print("You get eaten by a hungry shark. Game over.")
    elif choice1 == "wait":
        print("A boat arrives and you arrive at the island safely.")
        
    
        choice2 = input("You come to a cave. Do you want to venture inside or walk on? (venture/walk): ").lower()
        
        if choice2 == "venture":
            print("You are squished by boulders never to be seen again. Game over.")
        elif choice2 == "walk":
            print("You're at a crossroads.")
            
      
            choice3 = input("Do you go left, right, or straight? (left/right/straight): ").lower()
            
            if choice3 == "left":
                print("You are trampled by a herd of wildebeest. Game over.")
            elif choice3 == "straight":
                print("You get stung by a poisonous wasp. Game over.")
            elif choice3 == "right":
                print("You march on and find the buried treasure! Yippee!!")
            else:
                print("Invalid choice. Game over.")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")


treasure_island_adventure()
