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
		dict = {}
		lines = file.readlines()
		for line in lines:
			line = line.rstrip()
			line = line.replace('\n', '')
			result = [len(line.split())]
			countlines += 1
			for x in result:
				if x <= 10:
					tenorless.append(countlines)
					tenorless.append(line)
		print('\n'.join('{}' for _ in range(len(tenorless))).format(*tenorless))

		for x in tenorless:
			if key not in dict:
				dict[key] = tenorless.append(countlines)
			dict[value] = tenorless.append(lines)

		print(dict)

	wordCount()

main()
