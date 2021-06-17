#CLI VIRTUAL ASSISTANT

def main():
	run = True

	while run:
		command = input('>>')

		if command =='Hi':
			print('Hello!')
		elif command == 'exit':
			exit()
		else:
			print("couldn't process")

if __name__ == '__main__':
	main()

