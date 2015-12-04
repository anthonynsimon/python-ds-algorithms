from DataStructures import OrderedList

oList = OrderedList.OrderedList()
oList.add(7)
oList.add(0)
oList.add(5)

print(oList)
print("Size is {0}".format(oList.size()))

oList.remove(5)
oList.add(2)
oList.add(6)
oList.add(77)
oList.pop()
oList.pop()
oList.remove(0)
oList.pop()
print(oList)
print("Size is {0}".format(oList.size()))
print("Contains 2 ?", oList.search(2))
print("Contains 77 ?", oList.search(77))
