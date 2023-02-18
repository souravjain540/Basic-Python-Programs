message = 'Python is my favourite'
key=6
def en():
	ciphertext = [''] * key 
	for column in range(key):
		currentIndex = column
		while currentIndex < len(message):
			ciphertext[column] += message[currentIndex]
			currentIndex += key

	asd=''.join(ciphertext)
	print(asd)

def den(k):
	message='P  ryifitsath veomonyu'
	numOfColumns = int(math.ceil(len(message)/float(key)))
	numOfRows = k
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	plaintext=[''] * numOfColumns
	column=0	
	row=0
	for symbol in message:
		plaintext[column] += symbol
		column += 1 # Point to the next column.
		if (column == numOfColumns) or (column == numOfColumns - 1) and (row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1
	print(''.join(plaintext))

def brute(msg):
	for i in range(1,len(msg)):
		den(i)

en()
# den() #to dencrypt
# brute()	#to make brute force attack