# -*- coding: utf-8 -*-
"""Untitled31.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v6l23CwB974Jl25p8QFuUtPBO7Ts388F
"""

import random
import time
import os

print()
print('''\t\t\tWelcome to the \n\t\t\t\t
JACKPOT\t\t\t
You'll start with £50. You'll be asked if you want to play.
Answer with yes/no. you can also use y/n
There is no case sensitivity, type it however you like!
To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t£250
BELL\tBELL\tBELL/BAR\tpays\t£20
PLUM\tPLUM\tPLUM/BAR\tpays\t£14
ORANGE\tORANGE\tORANGE/BAR\tpays\t£10
CHERRY\tCHERRY\tCHERRY\t\tpays\t£7
CHERRY\tCHERRY\t  -\t\tpays\t£5
CHERRY\t  -\t  -\t\tpays\t£2
7\t  7\t  7\t\tpays\t The Jackpot!
''')
time.sleep(5)

#Constants:

INIT_STAKE = 50
INIT_BALANCE = 1000


ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]
# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Constructor to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
  
  
	# Given a reference to the head of a list
	# and a position, delete the node at a given position
	#This delete function code is contributed by Arabin Islam
	def deleteNode(self, position):
		if self.head is None:
			return
		if position == 0:
			self.head = self.head.next
			return self.head
		index = 0
		current = self.head
		prev = self.head
		temp = self.head
		while current is not None:
			if index == position:
				temp = current.next
				break
			prev = current
			current = current.next
			index += 1
		prev.next = temp
		return prev
  
	# Utility function to print the linked LinkedList

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data)
			temp = temp.next
  #Add new element at the end of the list

firstWheel = None
secondWheel = None
thirdWheel = None
fourthWheel=None
stake = INIT_STAKE
balance = INIT_BALANCE

def play():
    global stake, firstWheel, secondWheel, thirdWheel,fourthWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        fourthWheel=spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    global stake
    global balance
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (balance <=1):
            print ("Machine balance reset.")
            balance = 1000

        print ("The Jackpot is currently: £" + str(balance) + ".")
        answer = input("Would you like to play? Or check your money? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with £" + str(stake) + " in your hand. Great job!")
            time.sleep(5)
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("You currently have £" + str(stake) + ".")
        else:
            print("Whoops! Didn't get that.")
def endlinee():
  print ("\n\n**************************************************************************************\n\n")

def spinWheel():
    '''
    returns a random item from the wheel
    '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    '''
    prints the current score
    '''
    global stake, firstWheel, secondWheel, thirdWheel, balance
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 2
        balance = balance - 2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 5
        balance = balance - 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 7
        balance = balance - 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 10
        balance = balance - 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 14
        balance = balance - 14
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 20
        balance = balance - 20
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 250
        balance = balance - 250
    elif((firstWheel == "7") and (secondWheel == "7") and (thridWheel == "7")):
        win = balance
        balance = balance - win
    else:
        win = -1
        balance = balance + 1

    stake += win
    if win == balance:
        print ("You won the JACKPOT!!")
    if(win > 0):
        endlinee()
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win £' + str(win))
        endlinee()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        endlinee()
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')
        endlinee()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

play()

# Driver program to test above function
llist = LinkedList()
llist.push(thirdWheel)
llist.push(secondWheel)
llist.push(firstWheel)
ask=input("Do you want to re-do one of the spin for 2$ ?")
if (ask=='yes' or ask=='YES' or ask=='y' or ask=='Y'):
 llist.printList()
 q=input("Which of the following spin you want to re-do : ")
 stake=stake-2
 balance=balance+2
 if (q=='1'):
  llist.deleteNode(0)
  firstWheel=fourthWheel
  llist.push(firstWheel)
 elif (q=='2'): 
  llist.deleteNode(1)
  secondWheel=fourthWheel
  llist.push(secondWheel) 
 elif (q=='3'):
  llist.deleteNode(2)
  thiredWheel=fourthWheel
  llist.push(thiredWheel)
 else:
  exit
else:
  exit




printScore()
print("You ended the game with £" + str(stake) + " in your hand. Great job!")
play()

