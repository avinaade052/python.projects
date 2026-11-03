#ask the user roll the dice 
#then see if answer is y then print any two numbers 
#if the answer is n then print thankyou for playing 
# if anyhting else is printed insted of y and n then print invalid input 

from random import randint   
play = True 
while play:
    ask = input(("Roll the Dice ? (y/n) :")).lower()
    print(ask)
    if (ask == 'y') :
        die1 = randint(1,6)
        die2 = randint(1,6) 

        print (f'({die1}, {die2})')

    elif (ask == 'n') :
        print("Thankyou for playing !") 
        break 


    else :
        print("Invalid Input!")

 
