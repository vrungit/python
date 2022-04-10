from ast import Return
import random
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11,10]

def card_select(nu):
    return random.choices(cards,k=nu)


def blackjack(cList):
    if sum(cList) ==  21:
        return True
    else:
        return False
    

    
def check_ace(cList):
    print(f"Cards selected{cList}")
    for i in cList:
        if i == 11 :
            return True
    return False
        

#Computer Selection of first two cards and check for Ace and see blackjack score for 21
computer_first_select = card_select(2)
a = check_ace(computer_first_select)
if a == True:
   b =  blackjack(computer_first_select)
   if b == True:
       print("Compuer has ace and has a score of 21")


#User  Selection of first two cards
#user_first_select = card_select(2)

    



