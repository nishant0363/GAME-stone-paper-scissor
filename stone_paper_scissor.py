print( ''' 

                        YOU ARE WELCOMED TO THE MOST AWAITED GAME OF THE CENTURY
                                    STONE  PAPER SCISSORRRRRRRR !!!!!   
                        RULES  - YOU CAN ENTER ONLY ONE OF YOUR CHOICE FROM THE LIST
                                        [ STONE , PAPER , SCISSOR ] 
                        ENTER " NULL " TO EXIT   '''                  )
import random
a = input("Your Turn : ").lower()
i = 0
while i<50:
    if a == "null" :
        break
    

    l = [ "stone" , "paper" , "scissor" ]

    

    b = random.choice(l)
    
    if a == "stone" and b == "stone" :
        print("TIE !!!!!!!! ")
    if a == "stone" and b == "scissor" :
        print("YOU ARE THE WINNER !!!!!! ")
    if a == "stone" and b == "paper" :
        print("YOU LOST !!!!!! ")
    if a == "scissor" and b == "scissor" :
        print("TIE !!!!!!!! ")
    if a == "scissor" and b == "paper" :
        print("YOU ARE THE WINNER !!!!!! ")
    if a == "scissor" and b == "stone" :
        print("YOU LOST !!!!!! ")
    if a == "paper" and b == "paper" :
        print("TIE !!!!!!!! ")
    if a == "paper" and b == "scissor" :
        print("YOU LOST !!!!!! ")
    if a == "paper" and b == "stone" :
        print("YOU ARE THE WINNER !!!!!! ")
    if a== "paper" or a =="stone" or a =="scissor" :
        print("AS THE COMPUTER CHOOSED " + b )
    elif  a!= "paper" or a !="stone" or a !="scissor" or a !="NULL" :
        print(" WRONG INPUT . ONLY THREE CHOICES ALLOWED [ STONE , PAPER , SCISSOR ] ")   
    a = input("Your Turn : ").lower()    