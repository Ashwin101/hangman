import random
import os

BOARD = ['''
+--------+
|        |
|
|
|
|
|
|
==========
 ''' , '''
+--------+
|        |
|        O
|
|
|
|
|
========== 
''','''
+--------+
|        |
|        O
|       /
|
|
|
|
==========
''','''
+--------+
|        |
|        O
|       / \\
|
|
|
|
==========
''','''
+--------+
|        |
|        O
|       / \\
|        |
|
|
|
==========
''','''
+--------+
|        |
|        O
|       / \\
|        |
|       /
|
|
==========
''','''
+--------+
|        |
|        O
|       / \\
|        |
|       / \\
|
|
==========
''']

WORDLIST = 'australia arrow algebra bat board boston brazil banana coriander clam canada croissant crane crowbar dam django \
dinasour dessert eagle fanta fox fuse gamer germany hawk lionardo lumbini lamb mole money manchester mouse mother norway \
nitrogen omnipotent opeth pantera panda pokhara python rock room rat raven rhino silver seal shark sheep setsquare server \
snake spider student swan tentacle toad turnip turkey turtle window white wolf whisper zootopia'.split()

guessed_list = []


def welcome_screen():	#prints the welcome screen
	print '''
	
	 __                                                 
	|  |__ _____    ____    ____   _____ _____    ____  
	|  |  \\\\__  \  /    \  / ___\ /     \\\\__  \  /    \ 
	|   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \\
	|___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
	     \/     \/     \//_____/       \/     \/     \/ 


                  ******WELCOME TO HANGMAN******
       
       The rules are simple.. you just need to guess the word in 6 tries...
       Press Enter To Play
	'''
	flag = raw_input()
	os.system('clear')
	return

def get_rand_word():	#gets random word from the wordlist
	WordIndex = random.randint(0, len(WORDLIST)-1) 
	return WORDLIST[WordIndex]

def print_blanks(ans_word, guessed_letter = None):
	
	if guessed_letter == None:		#if nothing passed, prints blanks equal to length of the word
		print '_ ' * len(ans_word)
		return
	
	guessed_list.append(guessed_letter)

	for i in range(0, len(ans_word)):		
		if guessed_letter == ans_word[i]:
			print guessed_letter,
		elif ans_word[i] in guessed_list:
			print ans_word[i],

		else:
			print "_",
	check_if_won(ans_word, guessed_letter)

def check_if_won(ans_word, guessed_letter):
	flag = 0
	for i in range(0, len(ans_word)):
		if ans_word[i] in guessed_list:
			flag = flag + 1
		if flag >= len(ans_word):
			print "\nCongratulation you've guessed correctly"
			exit(0)

def get_user_input():
	print "\n\nEnter the letter: "
	guessed_letter = raw_input()
	return guessed_letter

def update_board(count = 0):
	print BOARD[count]
	heart_symbol = u'\u2764'
	heart = 'Lives Remaining: ' + (6 - count) * heart_symbol
	print heart

def main():
	life = 0
	welcome_screen()
	ans_word = get_rand_word()
	update_board()
	print_blanks(ans_word)
	while life < 6:
		guessed_letter = get_user_input()
		if len(guessed_letter) != 1 or guessed_letter not in 'abcdefghijklmnopqrstuvwxyz':		# to check if input is valid
			os.system('clear')
			update_board(life)
			print_blanks(ans_word, guessed_letter)
			print '\n\nPlease enter a valid character'
			continue
		
		elif guessed_letter in guessed_list:
			os.system('clear')
			update_board(life)
			print_blanks(ans_word, guessed_letter)
			print '\n\nAlready guessed.Guess again:'
			continue

		elif guessed_letter in ans_word:
			os.system('clear')
			update_board(life)
			print_blanks(ans_word, guessed_letter)
		
		
		else:
			life = life + 1
			os.system('clear')
			update_board(life)
			print_blanks(ans_word, guessed_letter)

	print "\n\n\nSorry you've run out of lives!!!"
	print "\n\nThe word was " + ans_word



	
if __name__ == '__main__':
	main()
