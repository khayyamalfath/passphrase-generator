'''passphrase-generator'''

'''
TO DO:
add it wordlist
add passphrase entropy
write help_text
write README.md
clean code
'''

import secrets

def main():
	en_wordlist = {}
	with open('diceware.wordlist.asc', 'r') as file:
		lines = file.readlines()

		for i, line in enumerate(lines, start=1):
			if 3 <= i <= 7778:
				dice, word = line.strip().split()
				en_wordlist[dice] = word
	
	help_text = '''help_text'''
	print(help_text)
	while True:
		input_string = input()
		tokens = input_string.split(' ')
		command = tokens[0]
		args = tokens[1:]

		if command == 'passphrase':
			print(f'Generate passphrase with args: {args}')
		elif command == 'help':
			if args:
				print(f"Error: 'help' command does not take any arguments. Invalid arguments: {args}")
			else:
				print(help_text)
			continue
		elif command == 'exit':
			if args:
				print(f"Error: 'exit' command does not take any arguments. Invalid arguments: {args}")
				continue
			else:
				break
		elif command == '':
			continue
		else:
			print(f'Error: invalid command: \'{command}\'')
			continue

		# default args
		wordlist = en_wordlist
		n_of_words = 5

		invalid_args = []
		for arg in args:
			if arg == 'en':
				wordlist = en_wordlist
			elif arg.isdigit():
				n_of_words = int(arg)
			else:
				invalid_args.append(arg)

		if invalid_args:
			print(f'Error: invalid arguments: {invalid_args}')
			continue

		passphrase = []
		for i in range(n_of_words):
			dice_roll = ''
			for _ in range(5):
				dice_roll += str(secrets.randbelow(6) + 1)
			passphrase.append(wordlist[dice_roll])
		print('\t'.join(passphrase))


if __name__ == '__main__':
	main()