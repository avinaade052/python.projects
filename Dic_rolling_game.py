#ask the user roll the dice 
#then see if answer is y then print any two numbers 
#if the answer is n then print thankyou for playing 
# if anyhting else is printed insted of y and n then print invalid input 

from random import randint #also use as import random #again for this * 
play = True 
while play:
    ask = input(("Roll the Dice ? (y/n) :")).lower()
    print(ask)
    if (ask == 'y') :
        die1 = randint(1,6)#and needed ramdom.randint(a,b)
        die2 = randint(1,6)#same as above 

        print (f'({die1}, {die2})')

    elif (ask == 'n') :
        print("Thankyou for playing !") 
        break 


    else :
        print("Invalid Input!")

#what i've learned in this project is that to exicuted the basics of python and core concepts
#i've used while loop int this for running this again and again and used import statement that is used for importing random number from 1 to 6 like in dice 
#then we've used if a=, elif and else conditions and printed the conditions and then we've used the printed the answer 
#this is a pyhton file . this is a pyhton file . 