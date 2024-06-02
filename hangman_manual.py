if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = "ABHIJIT"
	guessed = "_" * len(word)
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
	letter = input("guess letter: ")

	if letter.upper() not in word:
		print("Wrong guess.")

	while True:
		if letter in lstGuessed:
			letter = ''
			print("Already guessed!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter != '':
				lstGuessed.append(letter.upper())
			letter = input("Guess letter: ")

		if '_' not in guessed:
			print("You win")
			break 