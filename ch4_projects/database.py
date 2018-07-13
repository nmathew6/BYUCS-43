class Simpledb():

    def __init__(self, filename):

        self.filename = filename
        print("In __init__ of SimpleDB")
        # creating database before choices so if user enters anything other than 'a', program still works
        import os.path
        if os.path.exists(filename):
            print ('file exits')
        else:
            f = open(self.filename, 'w')
            f.close()


    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' file=' + self.filename + '>')

    # Save a new row into the database
    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()

    # Find and return one previously saved value with a matching key
    def select_one(self, key):
        f = open(self.filename, 'r')
        for line in f:
            line = line.strip()
            (k, v) = line.split('\t', 1)
            if k == key:
                return (v)

    # Delete all rows with the given key
    def delete(self, key):
        key_found = False
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
            else:
                key_found = True
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)
        return key_found

        # Change the values stored for the key

    def update(self, key, value):
        key_found = False
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                result.write(key + '\t' + value + '\n')
                key_found = True
            else:
                result.write(row)
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)
        return key_found


