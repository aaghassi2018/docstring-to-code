
def adventure():

    username = input("What's your name? ")

    print()
    print("Hey,", username, "welcome to the greatest adventure of your life.")
    print()
    print("The year is 1836 and you are currently settled in Jamestown. Your job is to try to get to your final destiantion: Pioneer, California without dying.")
    print()

    ready = input("Are you ready for your journey? [yes/no] ")

    if(ready == "yes"):
        print()
        print("You've started your journey and are well on your way... when suddenly, you've hit a rock and the wheel on your wagon has slightly broken.")
        wagon = input("Do you stop to fix the wheel or keep going? [fix the wheel/keep going] ")
        print()

        if wagon == "fix the wheel":
            print("Wise! Your adventure continues!")
            print()
            print()
            print("The next day you run into bandits that tell you that you must give them all of your belongins or they will kill you.")
            bandits = input("What do you do? [give them everything/try to run away] ")

            if(bandits == "give them everything"):
                print("You have elected to give them everything, including any and all food, as well as your wagon. You end up dying hours later.")
            elif(bandits == "try to run away"):
                print("Congratulations! You've successfully run away and you will continue your journey!")
                print()

                print("The next day, you run into a man who asks to hitch a ride.")
                man = input("Do you give him a ride? ")
                if(man == "yes"):
                    print()
                    print("You end up being friends with the man and all is well.")
                    print()

                    print("You have run out of food and you choose to kill and eat one of the people on the wagon with you.")
                    print("The names of the people on the wagon are: Carson, Cole, Rick, and Asa.")
                    print()
                    eat = input("Who do you decide to eat? [Carson/Cole/Rick/Asa ")

                    if(eat == "Carson"):
                        print("Poor choice. Carson's meat was not up to par with the level of meat that you need to survive. You die hours later.")
                    elif(eat == "Cole"):
                        print("Poor choice. Cole's meat was not up to par with the level of meat that you need to survive. You die hours later.")
                    elif(eat == "Asa"):
                        print("Poor choice. Asa's meat was not up to par with the level of meat that you need to survive. You die hours later.")
                    else:
                        print("Rick's meat was actually the only one who would supply you with enough nutrients to survive the rest of your jounrey. Congradulations! You've won!")
                    
                    
                elif(man=="no"):
                    print("He is unhappy with your decision and decides to pull out his gun and kill you.")
                else:
                    print("He is unhappy with your decision and decides to pull out his gun and kill you.")
        else:
            print("Later the same day, the wheel completley breaks and you are left to die overnight due to the lack of shelter. Oops!")
            print()

