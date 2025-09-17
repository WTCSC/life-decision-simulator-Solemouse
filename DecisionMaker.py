print("Welcome to the Lifeguard Life Simulator. You will type a number that corresponds to an option to answer a question.")

choice1 = input("\nA tungsten cube is drowning, what do you do: \n1 - Jump in the water \n2 - Spontaneously Combust \n3 - Throw a rescue tube at it\n> ")

if choice1 == "1":
    choice2 = input("\nYou are now in the water, what do you do?\n1 - Pick up the cube \n2 - Stand there menacingly\n> ")
    
    if choice2 == "1":
        choice3 = input("\nThe cube drags you under the water, what do you do?\n1 - Break physics \n2 - Drown\n> ")
        
        if choice3 == "1":
            if choice1 == "1" and choice2 == "1" and choice3 == "1":
                print("\nThe moment you attempt to break physics, the fabric of reality cannot withstand the contradiction.\nReality caves in on itself. You cease to exist. The cube still flies through a window.")
            else:
                choice4 = input("\nThe cube flies out of the water, do you let go mid-air?\n1 - Yes \n2 - No\n> ")
                
                if choice4 == "1":
                    print("\nYou fall back into the water and you look up as the cube flies through a window")
                elif choice4 == "2":
                    print("\nYou crash into a brick wall and get knocked down and you see the cube flying through a window.")
                else:
                    print("\nInvalid Input")
        
        elif choice3 == "2":
            print("\nYou drown and as you drown you see the cube flying through a window.")
        else:
            print("\nInvalid Input")
    
    elif choice2 == "2":
        choiceM = input("\nWhile you are standing there menacingly, the cube flies through a window, some moss slowly grows around your feet, do you fight the moss? \n1 - Yes \n2 - No\n> ")
        if choiceM == "1":
            print("\nThe moss notices your resistance, unhappy with your resistance, it crawls to your mouth and slowly suffocates you")
        elif choiceM == "2":
            print("\nThe moss is happy you don't resist, you slowly turn into moss, you are now part of the hive mind of moss, \nALL IS MOSS")
        else:
            print("\nInvalid Input")
    else:
        print("\nInvalid Input")

elif choice1 == "2":
    print("\nYou are now on fire.\nThe cube's smooth vertices crash into your flaming skull, the cube gets knocked off track and flies through a window\nYou die.")

elif choice1 == "3":
    choice5 = input("\nThe rescue tube is now floating in the water, what does the tube do?\n1 - Pick up the cube \n2 - Not pick up the cube\n> ")
    
    if choice5 == "1":
        print("\nThe tube drowns under the weight of the cube.\nThe cube flies out of the water and through a window.")
    elif choice5 == "2":
        print("\nYou fly into the sun and the cube flies through a window after quietly mentioning it has been sentient the whole time")
    else:
        print("\nInvalid Input")

else:
    print("\nInvalid Input")
