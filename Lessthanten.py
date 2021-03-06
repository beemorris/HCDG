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
		return f

	def wordCount():
		# gets the HC lines with <= 10 words
		file = getInputFile()
		tenorless = [] # creates a list for lines that are <= 10 words
		countlines = 0
		lines = file.readlines()
		match = [] # creates a list used for HC line numbers
		for line in lines:
			line = line.rstrip()
			line = line.replace('\n', '')
			tokenized = [len(line.split())] # tokenizes the sentence
			countlines += 1
			for x in tokenized:
				if x <= 10:
					match.append(countlines) # appends the line numbers to the list
					tenorless.append(line) # appends lines with <= 10 words to the list

		# gets the matching lines from the EN file
		file2 = getInputFile()
		lines2 = file2.readlines()
		matchedlines = [] #creates empty list of matchedlines
		countlines2 = 0 #
		counts = []# creates empty list for matches
		for line in lines2:
			line = line.rstrip()
			line = line.replace('\n', '')
			countlines2 += 1
			counts.append(countlines2)
			for x in match:
				if x == countlines2:
					matchedlines.append(line)


		#creates a tab delimited csv file where HC is on the left and EN is on the right
		f = open('output.tsv', 'w')
		for i, j in zip(tenorless, matchedlines):
			f.write(str(i) + "\t" + str(j) + '\n')
		f.close()

	wordCount()

main()
