def boggle (wordlist = []):
	runsum= 0

	for word in wordlist:
	
		if len(word) <= 4:
			runsum += 1
		elif len(word) == 5:
			runsum += 2
		elif len(word) ==6:
			runsum += 3
		elif len(word) ==7:
			runsum += 5
		else: 
			runsum += 11
	print(runsum)

	
boggle(['cat', 'tea', 'mate', 'computer', 'ale', 'bat'])

