'''
Hangman 9/22/19


'''
import random as rand

#option to show a random letter
#Make a tkinter gui
#Scrape a dictionary

words = [
    'people',
    'history',
    'way',
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power'
    ]

def intro():
	print("Welcome to Hangman! Try to guess the word!\n\n")
	#more rules

def print_cur_word(word, guesses):
	constructed_word = [" "]*len(word)

	for char in guesses:
		for index in range(len(word)):
			if(char == word[index]):
				constructed_word[index] = char

	print(constructed_word)

def play():
	selected_word = words[rand.randint(0, len(words)-1)]
	print("\t" + "_"*len(selected_word)+"\n\n")
	print("Enter your guess: ")
	incorrect = 0
	correct = 0
	chosen_words = []

	while(incorrect < len(selected_word)):
		char = input()
		#add hist option
		if(char in chosen_words):
			print('Word already chosen')
		elif(char in selected_word):
			print('Great')
			chosen_words.append(char)
			correct += list(selected_word).count(char)
			if(correct == len(selected_word)):
				print("Congratulations! You win!")
				break
		else:
			print('WRONG!')
			chosen_words.append(char)
			incorrect += 1
		print_cur_word(selected_word, set(chosen_words))

	print_cur_word(selected_word, set(chosen_words))

intro()
play()