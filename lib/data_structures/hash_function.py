class hash_function(object):

    def __init__(self, table_size):
        self.distribution_table = {}
        self.table_size = table_size

    def remainder_hash(self, number):
        hash_value = number % self.table_size
        self.add_to_table(hash_value)

    def add_to_table(self, key):
        if key in self.distribution_table:
            self.distribution_table[key] += 1
        else:
            self.distribution_table[key] = 1

    def clear_table(self):
        self.distribution_table.clear()


hash = hash_function(13)
for i in range(260):
    hash.remainder_hash(i)

print(hash.distribution_table)