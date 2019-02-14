def evens(numlist=[]):
	evenlist = []
	for i in range (len(numlist)):
		if numlist[i] % 2 == 0:
			evenlist.append(numlist[i])
	print(evenlist)
evens([3,9,4,5,2,8,9,2])
evens([6,6,3,12,5])
evens([3,5,9])
