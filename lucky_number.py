# this python program prints out a lucky number between 1 to 100
# a person puts his hand in a jar and takes out some dice
# and then rolls the dice on table
# the sum of the numbers onthe dice is your lucky number


import random 
import math
from random import randint
  
  
x = "y"

dice_dict={'face1':'[1]','face2':'[2]','face3':'[3]','face4':'[4]','face5':'[5]','face6':'[6]'}


 
while x == "y": 

    lucky_number_range= randint(1,100)

    #print(lucky_number_range)
    # now find the number of dice required
    if (lucky_number_range) <= 6:
        number_of_dice =1
    elif (lucky_number_range)%6==0:
        number_of_dice = math.trunc((lucky_number_range)/6)
    else:
        number_of_dice = math.trunc((lucky_number_range)/6) + 1


     
    randomlist=[] 
    #Generate 5 random numbers between 10 and 30
    for i in range(number_of_dice):
        randomlist.append(randint(1,6))

    
    
    dice_face=[]  
    for i in randomlist:
        dice_face.append('face'+str(i))
        
    display=[] 
    for i in dice_face:
        display.append(dice_dict[i])

    print(display)    

         
   
     
    print('You took out', len(randomlist),'nos of dice')
    print('your lucky number today is',sum(randomlist))
    x=input("press y to find your lucky number and n to exit:") 
    print("\n") 



 