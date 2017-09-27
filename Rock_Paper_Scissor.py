import random
list = ['rock','paper','scissor']
print("\n\t\t\t\tROCK PAPER AND SCISSOR GAME\n\n")
"""print("\t\t\t\t\t---->HERE IS YOUR CHOICE<----")
print("1.Single Player\n2.Two Player.")
choice= input("What  U Wnt to choose 1 or 2 :-")
"""
input0= input("\tEnter Your Name:-")

def GameSection(input0):
    c1= random.choice(list)
    print("\t\t\t\tComputer has been choosen :-")
    print(input0," Choose Your Choice b/w ROCK,PAPER or SCISSOR:-")
    c2= input()
    if(c1==c2):
        print("OH!!! Game Tie")
    elif(c1=='rock'):
        if(c2=='paper'): print("YoU WON! as Opponent Choose Rock")
        else: print("Opponent WON! as Choosen Rock ")
    elif(c1=='paper'):
        if(c2=='scissor'): print("YoU WON! as Opponent Choose Paper")
        else: print("Opponet WON! as Choosen Paper")
    elif(c1=='scissor'):
        if(c2=='rock'): print("YoU WON! as Opponent Choose Scissor")
        else: print("Opponent WON! as Choosen Scissor")
    TryInput= input("If U Want to Try Again Then Enter  Y or HIT Any Key :- ")
    if(TryInput=='y' or TryInput=='Y'):
        GameSection(input0)
    else:
        print("!!!THANK YOU FOR PLAYING!!!")
GameSection(input0)