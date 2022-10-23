# This class is to demonstate the how Hashmap generally works
# Feel free to make changes and play with it

class MyHashMap:
    def __init__(self, max_size=10):
        self.MAX_SIZE = max_size
        self.map = [None] * self.MAX_SIZE

    # function will return index in the array based on the key
    def _hash_function(self, key):
        if type(key) == str:
            hash_val = 0
            for i in range(len(key)):
                hash_val += ((i+1)*ord(key[i]))
        else:
            hash_val = int(key)

        return hash_val % self.MAX_SIZE

    # function to add key and value and
    # if key already present updates the value
    def add(self, key, val):
        idx = self._hash_function(key)
        if self.map[idx] is None:
            self.map[idx] = [[key, val]]
        else:
            if self.is_present(key):
                for i in range(len(self.map[idx])):
                    if self.map[idx][i][0] == key:
                        self.map[idx][i][1] = val
            else:
                self.map[idx].append([key, val])

    # returns value if key exits
    # else raises an error
    def get(self, key):
        if self.is_present(key):
            idx = self._hash_function(key)
            for key_val in self.map[idx]:
                if key_val[0] == key:
                    return key_val[1]
        else:
            raise KeyError("Key: {} doesn't exist".format(key))

    # deletes a value if key exists
    # else raises error
    def delete(self, key):
        if self.is_present(key):
            idx = self._hash_function(key)
            for i in range(len(self.map[idx])):
                if self.map[idx][i][0] == key:
                    del self.map[idx][i]
        else:
            raise KeyError("Key: {} doesn't exist".format(key))

    # returns True if key exists
    # else False
    def is_present(self, key):
        idx = self._hash_function(key)

        if self.map[idx] is None:
            return False

        for key_val in self.map[idx]:
            if key_val[0] == key:
                return True

        return False


if __name__ == '__main__':
    h = MyHashMap()
    h.add('name', "Hari")
    h.add('roll', 202089)
    h.add('name', "kiran")
    h.add(3.2, 'float')
    print(h.get('name'))
    print(h.get('roll'))
    print(h.get(3.2))
