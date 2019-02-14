def shortWords (stringList = []):
	list2 = []
	for word in stringList:
		if len(word) == 1 or len(word) ==2:
			list2.append(word)
	print(list2)
	
shortWords(['I', 'python', 'to', 'or', 'candy', 'as'])
shortWords(['wonder', 'to', 'beach', 'me'])
shortWords(['toolong', 'waytoolong'])