import hashlib

def hasher(text):
    converted=text.encode('utf-8')    
    return hashlib.sha256(converted).hexdigest()

def blacklist_write(usrnm,passwd):
    string=f"{usrnm}-{passwd}"
    with open("blacklisted.secure","a") as f1:
        f1.write(string+"\n")

def blacklist_read():
    try:
        with open("blacklisted.secure","r") as f1:
            return [i.strip() for i  in f1.readlines()]
    except FileNotFoundError:
        return []

def whitelist_write(usrnm,passwd):
    string=f"{usrnm}-{passwd}"
    with open("whitelisted.secure","a") as f2:
        f2.write(string+"\n")

def whitelist_read():
    try:
        with open("whitelisted.secure","r") as f2:
            return [i.strip() for i in f2.readlines()]
    except FileNotFoundError:
        return []

while True:
    print('Account Creation\n[1] Register\n[2] Login')
    opt=input("Option: ")
    if (opt=="1"):
        usrnm=hasher(input("Enter Username: ").lower())
        passwd=hasher(input("Enter Password: "))
        check=(f"{usrnm}-{passwd}") in whitelist_read()
        if (not check):
            whitelist_write(usrnm,passwd)
        else:
            print("User Already Exists!")
        break
    elif (opt=="2"):
        usrnm=hasher(input("Enter Username: ").lower())
        passwd=hasher(input("Enter Password: "))
        is_blacklisted=(f"{usrnm}-{passwd}") in blacklist_read()
        is_whitelisted=(f"{usrnm}-{passwd}") in whitelist_read()
        if (is_whitelisted and not is_blacklisted):
            print("Login Successful!")
            break
        elif (is_blacklisted and not is_whitelisted):
            print("Blacklisted Account! Access Denied!")
            break
        else:
            print("Invalid Credentials!")
    else:
        print("Invalid Option!")
