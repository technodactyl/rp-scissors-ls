from random import randint
from getpass import getpass
from time import sleep

def move(choice):#-------------------------------------------*Function to convert numeric choice into one of 5 plays.
	if(choice == 1):
		return "rock"
	elif(choice == 2):
		return "paper"
	elif(choice == 3):
		return "scissors"
	elif(choice == 4):
		return "lizard"
	elif(choice == 5):
		return "spock"

def play():#-------------------------------------------------*Function for player to select choice from 1-5.
        while(True):
                u_choice = getpass("Type to choose from 1.Rock, 2.Paper, 3.Scissors, 4.Lizard, and 5.Spock!\nPress one no. once and then press Enter.\n")
                if(u_choice.isdigit() == True):#-------------*If input is numeric,
                        u_choice = int(u_choice)#------------*convert to int
                        if(u_choice >= 1 and u_choice <= 5):#*and if it lies between 1 & 5
                                u_choice = move(u_choice)#---*call move on this choice, convert to string
                                break
                        else:#--------------------------------if it is not between 1 & 5
                                print("Oops, that doen't look quite right. Put in a number between 1 & 5.")
                                continue #-------------------*go back to beginning of loop, ask again.
                elif(u_choice == "" or u_choice == " "):
                        print("Oops, you can't leave this field blank.")
                        continue #---------------------------*go back to beginning of loop, ask again.
       	        elif(u_choice.isdigit() == False):
                        print("Oops, did you input a number between 1 & 5?")
       	                continue #---------------------------*go back...
#--------------Whenever a function contains a loop like this, it can be assumed that it keeps asking unless input is correct.
        return u_choice

class Player:#-----------------------------------------------*Player class.
        def __init__(self, name):
                self.name = name

        score = 0 #------------------------------------------*initializing score value to 0.
        choice = "" #----------------------------------------*initializing choice value.

        def choose(self):
                self.choice = play() #-----------------*method to select choice for player.
                
        def win(self):#--------------------------------------*method to increase score when won.
                print(self.name + " wins this round!\n")
                self.score += 1

class Computer(Player):#-------------------------------------*Computer object, inheriting from player object.
        def choose(self):#-----------------------------------*Replacing its choose method with random number selection from 1 to 5
                comp_choice = randint(1, 5)
                comp_choice = move(comp_choice)
                self.choice = comp_choice

user1 = Player("Player 1")#----------------------------------*Players 1 & 2, and the Computer
user2 = Player("Player 2")
computer = Computer("Computer")

def compare(player1=Player, player2=Player):#------------------------------*Function to compare player choices.
	if (player1.choice == player2.choice):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		print("The result is a tie!\n")
		return 0
	elif(player1.choice == "rock"):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		if(player2.choice == "scissors"):
			print("Rock breaks scissors.\n")
			return 1
		elif(player2.choice == "lizard"):
			print("Rock crushes lizard.\n")
			return 1
		elif (player2.choice == "paper"):
			print("Paper covers rock.\n")
			return 2
		elif (player2.choice == "spock"):
			print("Spock vaporizes rock.\n")
			return 2
	elif(player1.choice == "paper"):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		if(player2.choice == "rock"):
			print("Paper covers rock.\n")
			return 1
		elif(player2.choice == "spock"):
			print("Paper disproves Spock.\n")
			return 1
		elif(player2.choice == "scissors"):
			print("Scissors cuts paper.\n")
			return 2
		elif(player2.choice == "lizard"):
			print("Lizard eats paper.\n")
			return 2
	elif(player1.choice == "scissors"):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		if(player2.choice == "paper"):
			print("Scissors cuts paper.\n")
			return 1
		elif(player2.choice == "lizard"):
			print("Scissors decapitates lizard.\n")
			return 1
		elif(player2.choice == "rock"):
			print("Rock breaks scissors.\n")
			return 2
		elif(player2.choice == "spock"):
			print("Spock smashes scissors.\n")
			return 2
	elif(player1.choice == "lizard"):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		if(player2.choice == "paper"):
			print("Lizard eats paper.\n")
			return 1
		elif(player2.choice == "spock"):
			print("Lizard poisons Spock.\n")
			return 1
		elif(player2.choice == "rock"):
			print("Rock crushes lizard.\n")
			return 2
		elif(player2.choice == "scissors"):
			print("Scissors decapitates lizard.\n")
			return 2
	elif(player1.choice == "spock"):
		print("\n" + player1.name + " = " + player1.choice + "\t" + player2.name + " = " + player2.choice + "\n")
		if(player2.choice == "rock"):
			print("Spock vaporizes rock.\n")
			return 1
		elif(player2.choice == "scissors"):
			print("Spock smashes scissors.\n")
			return 1
		elif(player2.choice == "lizard"):
			print("Lizard poisons Spock.\n")
			return 2
		elif(player2.choice == "paper"):
			print("Paper disproves Spock.\n")
			return 2

def game(n, player1=Player, player2=Player):#----------------*The actual game starts here.
        r = 1 #----------------------------------------------*round number, initialized as 1
        if(n != 1):#-----------------------------------------*If number of rounds param is not equal to 1, multi-round game...
                length = (2 * n) - 1
                print(player1.name + " versus " + player2.name + ", Best of " + str(length) + ".\nFirst to " + str(n) + " wins!\n")
                sleep(0.75)
        else: #----------------------------------------------*...else, single game.
                print(player1.name + " versus " + player2.name + ", Single game.")
                sleep(0.75)
        while(player1.score != n and player2.score != n):#---*game goes on till someone reaches n first.
                print("Round " + str(r))
                sleep(0.75)
                player1.choose()
                player2.choose()
                g_round = compare(player1, player2)
                sleep(0.75)
                if(g_round == 0):
                      sleep(0.75)
                      print("Scores:")
                      print(player1.name + " = " + str(player1.score) + "\t" + player2.name + " = " + str(player2.score) + "\n")
                      sleep(0.75)
                      continue
                elif(g_round == 1):
                      player1.win()
                      sleep(0.75)
                elif(g_round == 2):
                      player2.win()
                      sleep(0.75)
                print("Scores:")
                print(player1.name + " = " + str(player1.score) + "\t" + player2.name + " = " + str(player2.score) + "\n")
                sleep(0.75)
                r += 1
        if(player1.score == n):
                print(player1.name + " wins the game!\n")
                sleep(0.75)                
        elif(player2.score == n):
                print(player2.name + " wins the game!\n")
                sleep(0.75)

def ask_for_name(player=Player):#-----------------------------------------*Function to ask for name
        while(True):
                u_name = input()
                if(u_name == ""):#----------------------------------------*if input is blank
                      print("Whoops! Your name can't be blank, silly!")
                      sleep(0.75)
                      continue
                else:
                      break
        split = u_name[1:]#-----------------------------------------------*Extract everything after first letter
        letter = u_name[0:1]#---------------------------------------------*extract first letter
        letter = letter.upper()#------------------------------------------*convert first letter to uppercase
        u_name = letter + split#------------------------------------------*add them together
        player.name = u_name#---------------------------------------------*save as class.name attribute

def ask_for_rounds():#----------------------------------------------------*Function to ask for number of rounds
        while(True):
                rounds = input("How many rounds to win?\nEnter a number between 1 & 7.\n")
                if(rounds != "" and rounds != " " and rounds != "0" and rounds.isdigit() == True and int(rounds) <= 7):
                      break
                elif(rounds == "0"):
                      print("Oops! Not a valid value. Please enter a number greater than 0.")
                      sleep(0.75)
                      continue
                elif(rounds == "" or rounds == " "):
                      print("Oops! Not a valid value. Please enter a non-blank value.")
                      sleep(0.75)
                      continue
                elif(rounds.isdigit() == False):
                      print("Oops! Not a valid value. Please enter a numeric value.")
                      sleep(0.75)
                      continue
                elif(int(rounds) > 7):
                      print("That's too many rounds! Please choose a number lower than 7.")
                      sleep(0.75)
                      continue
        rounds = int(rounds)
        return rounds

def doubleplayer():#-------------------------------------------------------Multiplayer mode.
        print("Hi!")
        print("Enter your name, Player 1!\n")
        ask_for_name(user1)
        print(user1.name + ' ready!\n')
        print("Enter your name, Player 2!\n")
        ask_for_name(user2)
        print(user2.name + ' ready!\n')
        while(True):
                rounds = ask_for_rounds()
                print("Flipping a coin...")#-------------------------------Randomly deciding order of play.
                sleep(2)
                coin = randint(1,2)
                if(coin == 1):
                        print("Heads! " + user1.name + " goes first!\n")
                        sleep(0.75)
                        game(rounds, user1, user2)
                if(coin == 2):
                        print("Tails! " + user2.name + " goes first!\n")
                        sleep(0.75)
                        game(rounds, user2, user1)
                leave = input("Wanna go again? (yes or y, any other key to exit)")
                if(leave == 'y' or leave == "yes"):
                        continue
                else:
                        break

def singleplayer():
        print("Hi!")
        sleep(1)
        print("What's your name?")
        ask_for_name(user1)
        print('That\'s a nice name, ' + user1.name + '!')
        sleep(0.75)
        while(True):
                rounds = ask_for_rounds()
                game(rounds, user1, computer)
                leave = input("Wanna go again? (yes or y, any other key to exit)\n")
                if(leave == 'y' or leave == "yes"):
                        continue
                else:
                        break

def menu():
        while(True):
                print("Welcome to Rock-Paper-Scissors-Lizard-Spock!\n")
                print("1. Vs. Computer")
                print("2. 2-Player Battle")
                print("3. Exit")
                entry = input()
                entry = int(entry)
                if(entry == 1):
                        singleplayer()
                elif(entry == 2):
                        doubleplayer()
                elif(entry == 3):
                        print("Thanks for playing!\n")
                        break
                else:
                        print("That doesn't look right. Enter a number between 1 & 3.")

menu()

