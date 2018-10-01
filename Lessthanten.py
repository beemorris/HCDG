def main():

	def getInputFile():
		bad = True
		while bad:
			try:
				fileName = input("Enter file name: ")
				# Open file for input
				f = open(fileName, "r")  # Note: "r" means open for reading.
				bad = False
			except Exception as err:
				print("Please enter a valid file name:")
		return f


	def wordCount():
		file = getInputFile()
		tenorless = []
		countlines = 0
		lines = file.readlines()
		match = []
		for line in lines:
			line = line.rstrip()
			line = line.replace('\n', '')
			result = [len(line.split())]
			countlines += 1
			for x in result:
				if x <= 10:
					match.append(countlines)
					tenorless.append(line)
		print('\n'.join('{}' for _ in range(len(tenorless))).format(*tenorless), file=open("output_hc.txt", "a"))


		file2 = getInputFile()
		lines2 = file2.readlines()
		matchedlines = []
		countlines2 = 0
		matches = []
		for line in lines2:
			line = line.rstrip()
			line = line.replace('\n', '')
			countlines2 += 1
			matches.append(countlines2)
			for x in match, matches:
				if x == x:
					matchedlines.append(line)

		print('\n'.join('{}' for _ in range(len(matchedlines))).format(*matchedlines), file=open("output_en.txt", "a"))

	wordCount()

main()
