'''
  * Class: 44-141 Computer Programming I
  * Author: ODERAH VALENTINE OSAKWE
  * Description: Program for Chute and Ladder with SIRI
  * Due: 10/18/2016
  * I pledge that I have completed the programming assignment independently.
  * I have not copied the code from a student or any source.
  * I have not given my code to any other student and will not share this code with anyone under any circumstances.
'''
#Main Program
#Use the print statements to display three messages

print("Programming is fun")
print("Welcome to Computer Programming")
print("Python is a programming language")

#import the random function
import random

#statr with your title
print("------------------------")
print(" Welcome to Dice Race!!!")
print("    Human vs Machine    ")

print("------------------------")

#Ask the user to enter his/her name
player = input("Who is player 1? ")

input("Press ENTER to begin")
print()

#firt play goes to the computer
siri1 = random.randint(1,6)  #because there is 2 dices from 1 to 6
siri2 = random.randint(1,6)  #create 2 random functions for the dice for siri
print("siri rolled the dice")
print("siri rolled a", siri1, "and", siri2)

traveled = 0 #keep track of user travel
totalSpaces = 50
siritravel = siri1 + siri2 #keep track of siri travel
round = 0
siriSpace = 50

#give user the opportunity to quit
quit = input("Enter 0 to quit")

#Use the while loop to integrate the play between user and siri
#As long as the user doesn't enter 0
while (quit != "0"):
    #use the first funtion to keep track of round and user travel
    if (traveled<50 and siritravel<50):
        round += 1
        print("----- Round",round,"-----")
        player1 = random.randint(1,6) #user first dice with random 1-6
        player2 = random.randint(1,6) #user second dice with random 1-6

        traveled += player1 + player2

         #used to create user Chute
        if (traveled%11==0):
            print("----But----")
            print("^^^^^^^^^^^^^^^^^^")
            print(player," just hit chute")
            print(player," has to go back to the start")
            print("^^^^^^^^^^^^^^^^^^")
            traveled == 0
            print()

            #keep track of player role
        else:
            print()
            print(player," rolled the dice")
            print("You rolled a",player1,"and",player2)
            print("you have", totalSpaces - traveled,"left to go")

        siri1 = random.randint(1,6) #siri dice 1 with random 1-6
        siri2 = random.randint(1,6) #siri dice 2 with random 1-6

        #siri chute
        if (siritravel%11==0):
            print("----But----")
            print("^^^^^^^^^^^^^^^^^^^^^^")
            print("siri just hit chute")
            print("siri has to go back to the start")
            print("^^^^^^^^^^^^^^^^^^^^^^")
            siritravel = 0
            print()

        else:
            #keep track of siri dice roll and travel
            print()
            print("siri rolled the dice")
            print("siri rolled a", siri1, "and", siri2)
            siritravel += siri1 + siri1
            print("siri has moved", siritravel,"spaces")

            #Always give user the opportunity to quit.
            quit = input("Press Enter to continue playing with siri (0 to quit):")
            print()

     #used to keep track of player winning the game
    elif(traveled>=50):
        print(player," got to 50 first and won")
        break #always looped so i used break to cancel after the first loop



    elif(siritravel>=50):
        print("siri got to 50 first and won")
        break  #always looped so i used break to cancel after the first loop
print("Game Over")
