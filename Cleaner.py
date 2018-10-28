def main():
	def getInputFile():
		bad = True
		while bad:
			try:
				fileName = input("Enter file name: ")
				# Open file for input
				f = open(fileName, "r")
				bad = False
			except Exception as err:
				print("Please enter a valid file name:")

	def clean():
		file = getInputFile()
		lines = file.readlines()
		for line in lines:
			line = line.rstrip()
			line = line.replace('\n', '')
			tokenized = [len(line.split())]  # tokenizes the sentence

		

	clean()

main()