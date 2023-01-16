def homoglyphs(phrase):

	homoglyph = []
	
	#Switch letters to homoglyphs
	for i in list(phrase):
		
		#If A
		if i.upper() == 'A':
		
			homoglyph.append("@")
		
		#If B
		elif i.upper() == 'B':
		
			homoglyph.append("|3")
		
		#If D
		elif i.upper() == 'D':
		
			homoglyph.append("|)")
		
		#If H 
		elif i.upper() == 'H':
		
			homoglyph.append("|-|")
		
		#If K
		elif i.upper() == 'K':
			
			homoglyph.append("|<")
		
		#If L	
		elif i.upper() == 'L':
		
			homoglyph.append("|_")
		
		#If M
		elif i.upper() == 'M':
		
			homoglyph.append("|V|")
		
		#If N
		elif i.upper() == 'N':
		
			homoglyph.append("|\|")
		
		#If O
		elif i.upper() == 'O':
		
			homoglyph.append("()")
		
		#If X
		elif i.upper() == 'X':
		
			homoglyph.append("><")
		
		#If anything else
		else:
		
			homoglyph.append(i)
	
	newhomoglyphphrase = (''.join(homoglyph))
	
	return newhomoglyphphrase
		
def acronym(phrase):
	
	acronyms = [["BTW"], ["LOL"], ["AFK"], ["NGL"]]
	
	newacronym = []
	
	temp_phrase = phrase
	
	#Look for "by the way"
	newphrase = temp_phrase.split("BY THE WAY")
	temp_phrase = "BTW".join(newphrase)
	
	#Look for "laughing out loud"
	newphrase = temp_phrase.split("LAUGHING OUT LOUD")
	temp_phrase = "LOL".join(newphrase)
	
	#Look for "away from keyboard"
	newphrase = temp_phrase.split("AWAY FROM KEYBOARD")
	temp_phrase = "AFK".join(newphrase)
	
	#Look for "not gonna lie"
	newphrase = temp_phrase.split("NOT GONNA LIE")
	temp_phrase = "NGL".join(newphrase)
	
	return temp_phrase
	
	#Look for 
	
	
def upper(phrase):
	
	capital = []
	
	#Changing lower to caps
	for i in list(phrase):
		
		#If already a capital or space
		if (ord(i) > 64 and ord(i) < 91) or ord(i) == 32:
		
			capital.append(chr(ord(i)))
		
		#If lower case
		elif ord(i) > 96 and ord(i) < 123:
		 
			capital.append(chr(ord(i) - 32)) 
		
		#For puncuations 
		else:
			
			capital.append(chr(ord(i)))
	
	newcapitalphrase = (''.join(capital))
	
	return newcapitalphrase

def main():
	
	#Ask user for phrase
	phrase = input("Give a phrase: ")
	
	no_punc = []
	
	#Getting rid of punctuations
	for i in list(phrase):
	
		#If already a capital
		if ord(i) > 64 and ord(i) < 91:
		
			no_punc.append(chr(ord(i)))
		
		#If lower case
		elif ord(i) > 96 and ord(i) < 123:
		 
			no_punc.append(chr(ord(i))) 
		
		#If a space
		elif ord(i) == 32:
			
			no_punc.append(chr(ord(i)))
	
		#If there are puncations
		else:
		
			no_punc.append(chr(0))
	
	#Phrase without puncuations
	no_punc = ''.join(no_punc)
	print(no_punc)
	
	#Print capitalized phrase
	capital = upper(no_punc)
	print(capital)
	
	#Acronym phrase
	acronym_phrase = acronym(capital)
	print(acronym_phrase)
	
	#Print homoglyph phrase
	homoglyph_phrase = homoglyphs(acronym_phrase)
	print(homoglyph_phrase)
	
main()
