words 	= ['zero', 'one', 'two', 'free', 'four', 'five']



def conntow(number): # convert number to word
	print(words[number])


def conwton(word): #convert word to number
	for i in range(6):
		if word == words[i]:
			print(i)
			break

		else:	i+=1

