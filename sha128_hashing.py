import hashlib

def sha128_hashing(string):
    return hashlib.sha1(string.encode()).hexdigest()


if __name__ == "__main__":
    string = input("Enter a string: ")
    print(sha128_hashing(string))
