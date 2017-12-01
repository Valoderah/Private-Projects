'''
  * Class: 44-141 Computer Programming I
  * Author: OsakweO and JeffriesV
  * Description: (Give a brief description for the exercise or project)
  * Due: 10/31/2016
  * We pledge that we have completed the programming assignment independently.
  * We have not copied the code from a student or any source.
  * We have not given our code to any other student and will not share this code with anyone under any circumstances.
'''
#Main Program
#Use the print statements to display three messages
print("Programming is fun")
print("Welcome to Computer Programming")
print("Python is a programming language")

import random

name = input("Enter your name: ")
name = name.capitalize()

#prompt user to enter string
print(name, end="")
word = input(", enter a phrase for the computer to guess(letters, numbers and spaces only): ")
word = word.lower()

#this is the list of possible characters
possibleCharacters = "abcdefghijklmnopqrstuvwxyz0123456789 "

#make good a variable to check if the chaRACTER IS LEGAL OR ILLEGAL
good = False

while (not good):
    good = True  #make good true so as to execute the loop
    for letters in word:
        if (possibleCharacters.find(letters) == -1):
            good = False #if user enters a good character, the loop terminates

    if(not good): #if you entered an illegal character
        print("You entered an illegal character")
        print(name, end="")
        word = input(", enter a phrase for the computer to guess(letters, numbers and spaces only): ")
        word = word.lower()

#used randomcharacter to check for the first character (to see if the first set matches).
randomCharacter = ""
for a in range (len(word)):
    randomCharacter += possibleCharacters[random.randint(0,36)] #used random to iterate through the characters.
print(randomCharacter)

count = 0
match = False

#used the while loop to iterate through the characters and search for the right character
while (match==False):
    randomCharacter2 = "" #Smart way of forcing the code to recognise randomcharacter2 for my iteration
    match = True

    for letters in range (len(word)): #goes through each of the characters
        if (word[letters] == randomCharacter[letters]): #if it matches retain
            randomCharacter2 += word[letters]

        elif (word[letters]!=randomCharacter[letters]):
            randomCharacter2 += possibleCharacters[random.randint(0,36)] #if not match check again
            match = False


    randomCharacter = randomCharacter2 #changes the value of randomcharacter after iteration

    print(randomCharacter)

    count += 1 #keeps track of count

print("Phrase matched! That took", count, "attempts" )


