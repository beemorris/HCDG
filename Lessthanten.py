import re
from collections import Counter
from nltk import word_tokenize

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
		fileHandler = getInputFile()
		tenorless = []
		lines = fileHandler.readlines()
		for line in lines:
			line = line.rstrip()
			line = line.replace('\n', '')
			result = [len(line.split())]
			for x in result:
				if x <= 10:
					tenorless.append(line)

	wordCount()

main()

