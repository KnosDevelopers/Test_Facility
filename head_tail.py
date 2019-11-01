#This is a console based open source head tail game, inspired by our own childhood!
#Try and test it vigorously so that errors are found
#Do tell my if any errors are found or simply correct it yourself and then highlight them to me
#Your feedback is highly appreciated!
#KNOS DEVS FOR LIFE!!!!!

#IMPORTING LIBRARIES

import random
import time

#TOSS CODE:

while True:
    toss = input("Enter your choice, press h for heads and t for tails: ")
    toss.lower()
    if(toss=='h' or toss=='t'):
        break
    else:
        print("Please input either h or t!")

while True:
    toss_number=input("Enter number for toss: ")
    if(int(toss_number)>0 and int(toss_number)<7):
        break
    else:
        print("Please enter number between 1 and 6!")

comp_toss_number=random.randint(1,6)
print("Computer has chosen ",comp_toss_number)

sum_of_toss = int(toss_number) + int(comp_toss_number)

toss_elect=""
bat_first= 0
time.sleep(.400)
if((sum_of_toss%2)==0 and toss=='t'):
    print("Congratulations you have won the toss!")
    toss_elect = "user"
elif((sum_of_toss%2)!=0 and toss=='h'):
    print("Congratulations you have won the toss!")
    toss_elect = "user"
else:
    print("So unfortunate, you have lost the toss :(")

if(toss_elect=="user"):
    while True:
        toss_decision = input("Bat or Bowl? >> ")
        if(toss_decision.lower()=="bat"):
            bat_first=1
            print("You have elected to",toss_decision.capitalize(),"first")
            break
        elif(toss_decision.lower()=="bowl"):
            print("You have elected to",toss_decision.capitalize(),"first")
            break
        else:
            print("Please choose either Bat or Bowl!")
else:
    toss_dec_list = ["Bat","Bowl"]
    toss_dec=random.choice(toss_dec_list)
    print("Computer has elected to",toss_dec,"first")
    if(toss_dec.lower()=="bowl"):
        bat_first==1


#ACTUAL MATCH:

total=0
total_comp=0
option=0
option_comp=0
if(bat_first==1):
    while True:
        while True:
            option=int(input("Enter number between 1 and 6: "))
            if(option<7 and option>0):
                break
            else:
                print("Please enter number between 1 and 6!")
        option_comp=random.randrange(1,6)
        print("Computer chose ",option_comp)
        if(option==option_comp):
            print("You are out, your total was",total)
            print("Now computer will bat!")
            break
        total+=option
        #####################################################
    while True:
        while True:
            option=int(input("Enter number between 1 and 6: "))
            if(option<7 and option>0):
                break
            else:
                print("Please enter number between 1 and 6!")
        option_comp=random.randrange(1,6)
        print("Computer chose ",option_comp)
        if(option==option_comp):
            print("Computer is out, total was",total_comp)
            break
        total_comp+=option_comp
        if(total_comp>total):
            print("Computer scored:",total_comp)
            break

########################
if(bat_first==0):
    while True:
        while True:
            option=int(input("Enter number between 1 and 6: "))
            if(option<7 and option>0):
                break
            else:
                print("Please enter number between 1 and 6!")
        option_comp=random.randrange(1,6)
        print("Computer chose ",option_comp)
        if(option==option_comp):
            print("Computer is out, total was",total_comp)
            print("Now you will bat!")
            break
        total_comp+=option_comp
    ##################################

    while True:
        while True:
            option=int(input("Enter number between 1 and 6: "))
            if(option<7 and option>0):
                break
            else:
                print("Please enter number between 1 and 6!")
        option_comp=random.randrange(1,6)
        print("Computer chose ",option_comp)
        if(option==option_comp):
            print("You are out, your total was",total)
            break
        total+=option
        if(total>total_comp):
            print("You scored:",total)
            break

if(total>total_comp):
    print("Congratulations you won!")
elif(total==total_comp):
    print("Would you believe it? It's a DRAW!!!!!")
else:
    print("SED YOU LOST!:( MA NAME IS JEFF")

