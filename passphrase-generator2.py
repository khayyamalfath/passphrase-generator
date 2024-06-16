'''passphrase-generator'''

def lexer(input_string):
	tokens = []
	i = 0
	length = len(input_string)

	while i < length:
		if input_string[i].isspace():
			i += 1
			continue
		
		matched = False

		for command in ['passphrase', 'help', 'exit']:
			if input_string.startswith(command, i):
				tokens.append(('COMMAND', command))
				i += len(command)
				matched = True
				break
		
		if matched:
			continue

		if input_string[i] == '-':
			start = i
			i += 1
			while i < length and input_string[i].isalnum():
				i += 1
			tokens.append(('ARG', input_string[start:i]))
			continue

		if input_string[i].isdigit():
			start = i
			while i < length and input_string[i].isdigit():
				i += 1
			tokens.append(('NUMBER', input_string[start:i]))
			continue

		raise ValueError(f'Invalid character: {input_string[i]}')
	
	return tokens

def parser(tokens):
	if not tokens:
		return None, []
	
	command = tokens[0][1]
	args = []
	for token in tokens[1:]:
		args.append(token[1])

	return command, args

def handle_command(command, args):
	if command == 'passphrase':
		print('passphrase')
	elif command == 'help':
		print('help')
	elif command == 'exit':
		print('exit')
		return False
	else:
		print('commando sconosciuto')

	return True

def main():
	welcome_screen = '''hello'''
	print(welcome_screen)
	while True:
		try:
			input_string = input('> ')
			tokens = lexer(input_string)
			command, args = parser(tokens)
			if command:
				if not handle_command(command, args):
					break
		except ValueError as e:
			print(e)
		except KeyboardInterrupt:
			print('keyboardinterrupt')
			break

main()