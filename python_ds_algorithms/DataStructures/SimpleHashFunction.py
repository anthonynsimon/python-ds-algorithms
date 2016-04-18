class SimpleHashFunction(object):

    def __init__(self, sizeOfTable):
        self.distributionTable = {}
        self.sizeOfTable = sizeOfTable

    def remainderHash(self, number):
        hashValue = number % self.sizeOfTable
        self.addToTable(hashValue)

    def addToTable(self, key):
        if key in self.distributionTable:
            self.distributionTable[key] += 1
        else:
            self.distributionTable[key] = 1

    def clearTable(self):
        self.distributionTable.clear()


hash = SimpleHashFunction(13)
for i in range(260):
    hash.remainderHash(i)

print(hash.distributionTable)