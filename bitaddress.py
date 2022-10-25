from bitcoin import *
#generate private key
private_key = random_key()
print("This is the private key, keep me safe : " + private_key)
#use the private to generate a public key
public_key = privtopub(private_key)
print("This is my public address: " + public_key)
 #your bitcoin address
address = pubtoaddr(public_key)
print("My btc address is : " + address + " you can send btc here")