import random
play = True

while play :
     
    if (play == True):
        print("Welcome to our number guessing game !")
    else:
        print("Thankyou for coming !")    


    gen = random.randint(1,50) 
     

    user = int(input("Guess the number in integer value (1 to 50): "))
    if ( gen > 50):
        print ("INVALID NUMBER !")
        break
    else:


        if (user > int(gen)):
             print("Too high !")
        elif (user < int(gen)):
            print("Too Low !")

        else :
            (user == int(gen))
            print("Congratulations ! You've got that !")


 