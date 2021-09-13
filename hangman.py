import random
def main():
	print("Hangman in Python")
	print('To exit the game type "bye"')
	print()
	f = open("word_list.txt")
	words = f.read() #.split(', ')
	f.close()
	words = words.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
	words = words.split(',')
	guess = []
	usrin = ""
	attempts = 11
	gword = random.choice(words)
	#print(gword)
	for i in gword:
		guess.append('_')
	while usrin != "bye":
		for i in guess:
			print(i, end=' ')
		print('\n')
		usrin = input('Your guess: ')
		x = 0
		for i in gword:
			if i.lower() == usrin.lower():
				print('Hit')
				guess[x] = i
			x += 1
		if usrin.lower() not in gword.lower():	
			attempts -= 1
			print('You have', attempts, 'attempts left')
		if '_' in guess:
			if attempts == 0:
				print('You lose')
				print('The word was: ', gword)
				break
		else:
			print('You won! The word was: ', gword)
			break
if __name__ == "__main__":
	main()
