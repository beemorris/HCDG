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

		file2 = getInputFile() # gets second file
		lines2 = file2.readlines() # reads in lines of second file
		matchedlines = [] #creates empty list of matchedlines
		countlines2 = 0 # initializes and sets to 0
		counts = []# creates empty list for matches
		for line in lines2: # iterates over the lines in a file
			line = line.rstrip() # strips the stuff from the right of lines
			line = line.replace('\n', '') # replaces the new line carriage return with nothing
			countlines2 += 1 # increments the countlines variable
			counts.append(countlines2) # appends the line counts
			for i in match if i in counts:
				print(matchedlines)
			'''
			for x in match: #iterates over the line counts with less than 10 words from wordCount()
				if x in counts:
					matchedlines.append(line) #this should only be appending the matched lines but it's appending all of them and idk why
				else:
					quit()
			'''

		#print(match)
		#print(counts)
		#print('\n'.join('{}' for _ in range(len(matchedlines))).format(*matchedlines), file=open("output_en.txt", "a"))


	wordCount()

main()
