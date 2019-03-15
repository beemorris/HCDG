import re

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

	def clean():
		gloss = []
		file = getInputFile()
		lines = file.readlines()
		for line in lines:
			line = line.rstrip()
			line = line.replace('poss', 'nmod:poss')
			line = line.replace('erg', 'ERG')
			line = line.replace('1PS', 'PRON')
			line = line.replace('3PS', 'PRON')
			line = line.replace('BE', 'AUX')
			line = line.replace('.III', '')
			line = line.replace('.PL', '')
			line = line.replace('2PS', 'PRON')
			line = line.replace('3SS', 'PRON')
			line = line.replace('1.ss', 'PRON')
			line = line.replace('1.sg', 'PRON')
			line = line.replace('1s.', '')
			line = line.replace('.II', '')
			line = line.replace('.2.SO', '')
			line = line.replace('3.SO', '3.SG')
			line = line.replace('prox.', '')
			line = line.replace('3SS.2.SO', 'PRON')
			line = line.replace('.1?', '')
			line = line.replace('COP', 'AUX')
			line = line.replace('3ss', 'PRON')
			line = line.replace('3s.POSS', 'PRON')
			line = line.replace('1ss', 'PRON')
			line = line.replace('1pls', 'PRON')
			line = line.replace('3ss', 'PRON')
			line = line.replace('3P.SUBJ', 'PRON')
			line = line.replace('3SG.SUBJ', 'PRON')
			line = line.replace('LOC', 'ADP')
			line = line.replace('INT', 'Q')
			line = line.replace('1SG', 'PRON')
			line = line.replace('3SG', 'PRON')
			line = line.replace('1SG', 'PRON')
			line = line.replace('2SG.SUBJ', 'PRON')
			line = line.replace('1S.S', 'PRON')
			line = line.replace('3S.O', 'PRON')
			line = line.replace('3S.S', 'PRON')
			line = line.replace('3S.O', 'PRON')
			line = line.replace('3P.S', 'PRON')
			line = line.replace('3S.POSS', 'PRON')
			line = line.replace('3.ss ', 'PRON')
			line = line.replace('1.so', 'PRON')
			line = line.replace('3.so', 'PRON')
			line = line.replace('3.SG', 'PRON')
			line = line.replace('3.SS', 'PRON')
			line = line.replace('-', '\t')
			line = line.replace('be.at', 'AUX')
			line = line.replace('3SS.2.SO', 'PRON')
			line = line.replace('3so', 'PRON')
			line = line.replace('3.ss', 'PRON')
			line = line.replace('<', '')
			line = line.replace('>', '')
			#line = line.split('\t')


			gloss.append(line)
		with open("bmglossingtransformed.txt", 'w') as f:
			print('\n'.join(gloss), file=f)

	clean()

main()
