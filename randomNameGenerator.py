"""
Ok, so...It works, but it's inconvenient. I want to be
able to add multiple names in the beginning of the 
program, so I think I can't use a list for that.
"""

import random
import sys

list = []

def getRandomName():
  length = len(list)
  length -=1
  newName = random.randint(0, length)
  print(list[newName])

def nameFunction():
  choice = input("Do you want to enter a name? (y/n) ")
  while choice == "y":
    name = input("Enter a name: ")
    list.append(name)
    print(list)
    choice = input("Do you want to enter a name? (y/n) ")

  if choice == "n":
    randomName = input("Do you want to select a random name? (y/n) ")
    if randomName == "y":
      if len(list) == 0:
        print("You did not enter any names.")
        nameFunction()
      else:
        getRandomName()
        randomName = input("Do you want to select a random name? (y/n) ")
        while randomName == "y":
          getRandomName()
          randomName = input("Do you want to select a random name? (y/n) ")
          if randomName == "n":
            sys.exit()
        if randomName == "n":
          sys.exit()
    elif randomName == "n":
      sys.exit()
    else:
      print("Invalid. Please try again.")
      nameFunction()
  else:
    print("Invalid. Please try again.")
    nameFunction()


nameFunction()

