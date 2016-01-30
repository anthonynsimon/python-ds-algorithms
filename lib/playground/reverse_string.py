from lib.data_structures.deque import Deque


def reverseString(string):
    deque = Deque()
    inputStr = str(string)
    items = []
    for ch in inputStr:
        deque.add_head(ch)
    for i in range(deque.size()):
        items.append(deque.remove_head())
    return "".join(items)

def reverseStringAlternative(string):
    inputStr = str(string)
    length = len(inputStr)
    items = []
    for i in range(length):
        items.append(inputStr[length - 1 - i])
    return "".join(items)


text = "Let's grab some lunch"
print(text)
text = reverseString(text)
print(text)
text = reverseStringAlternative(text)
print(text)
print(reverseStringAlternative(123456789))
print(reverseString("Let's go to XYZ"))