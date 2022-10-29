# msg = 'Vncqxm rw fqrlq njlq unccna rw cqn yujrwcngc rb anyujlnm kh j unccna bxvn orgnm wdvkna xo yxbrcrxwb mxfw cqn juyqjknc. Cqn vncqxm rb wjvnm jocna Sdurdb Ljnbja, fqx dbnm rc rw qrb yarejcn lxaanbyxwmnwln.'
msg = """Aopz jhlzhy jfwoly hbavthapjhssf klaljaz lujyfwalk tlzzzhnlz huk kljvklz aolt bzpun slaaly-mylxblujf huhsfzpz - aol svunly aol tlzzhnl, aol ilaaly!
"""
# list of a-z lowercase
letters = [chr(b) for b in range(ord('a'), (ord('z')+1))]

# import matplotlib.pyplot as plt

# returns decrypted caeser ciphers; anything thats not a letter is ignored
def decrypt(msg,offset):
	shift = 7-offset
	msg = msg.split(" ")

	dec = r""
	# Goes through each char; handles capitaliisation and ignores char if not part of letters list
	for eachWord in msg:
		for eachChar in eachWord:
			if eachChar.lower() in letters:
				if eachChar.isupper():
					eachChar = eachChar.lower()
					# Modulus used for wraparound on a list
					newL = (letters[(ord(eachChar)+shift)%len(letters)])
					newL = newL.capitalize()
					dec += newL
				else:

					# newL = chr(ord(eachChar)-shift)
					(ord(eachChar)-shift)%len(letters)
					newL = (letters[(ord(eachChar)+shift)%len(letters)])
					dec += newL
			else:
				dec += eachChar
		# space after each word
		dec += " "
	return dec

# Decrypts caeser ciphers using simple frequency analysis
def autodecrypt(msg):

	freq = []
	# Go through all letters and store their frequency in the message in a list
	for eachL in letters:
		letterCount = msg.count(eachL)
		freq.append(letterCount)

	# Calculate how much the shift is
	highestIndex = freq.index(max(freq))
	shift = highestIndex-4 # 'e' is the 4th element in letters list
	print(decrypt(msg,shift))
	# print()
	# print(letters[highestIndex])
	# plt.plot(letters,freq)
	# plt.show()


print(decrypt(msg,7))
autodecrypt(msg)