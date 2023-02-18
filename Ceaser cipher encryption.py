#cryptography-Ceaser Cipher
txt='Python?'
txt=txt.upper()
key=10
en=''
mode='e'
encode=''
char_index=0
en_index=0
alpha_num='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .?'
for letters in txt:
	if letters in alpha_num:
		if mode=='e':
			char_index=alpha_num.find(letters)
			en_index=char_index+key
		elif mode=='d':
			char_index=alpha_num.find(letters)
			en_index=char_index-key

		if en_index>=len(alpha_num):
			en_index=en_index-len(alpha_num)

		if en_index<0:
			en_index+=len(alpha_num)

	en+=alpha_num[en_index]

print(en)