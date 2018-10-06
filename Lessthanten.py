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
		print('\n'.join('{}' for _ in range(len(tenorless))).format(*tenorless), file=open("output_hc.txt", "a")) #makes it pretty

		file2 = getInputFile()
		lines2 = file2.readlines()
		matchedlines = [] #creates empty list of matchedlines
		countlines2 = 0 #
		counts = []# creates empty list for matches
		for line in lines2:
			line = line.rstrip()
			line = line.replace('\n', '')
			countlines2 += 1
			counts.append(countlines2) # appends the line counts
			for x in match, counts: #iterates over the line counts with less than 10 words from wordCount()
				if x == x:
					matchedlines.append(line) #this should only be appending the matched lines but it's appending all of them and idk why

		print(matchedlines)
		#print(match)
		#print(counts)
		#print('\n'.join('{}' for _ in range(len(matchedlines))).format(*matchedlines), file=open("output_en.txt", "a"))


	wordCount()

main()
