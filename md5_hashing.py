import hashlib


def md5_hashing(string):
    return hashlib.md5(string.encode()).hexdigest()


if __name__ == "__main__":
    string = input("Enter a string: ")
    print(md5_hashing(string))
