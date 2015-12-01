import Deque

def reverseString(string):
    deque = Deque.Deque()
    inputStr = str(string)
    outputStr = ""

    for ch in inputStr:
        deque.addHead(ch)

    for i in range(deque.size()):
        outputStr += deque.removeHead()

    return outputStr

def reverseStringAlternative(string):
    inputStr = str(string)
    outputStr = ""
    length = len(inputStr)

    for i in range(length):
        outputStr += inputStr[length - 1 - i]

    return outputStr

text = "Let's grab some lunch"
print(text)
text = reverseStringAlternative(text)
print(text)
text = reverseStringAlternative(text)
print(text)
print(reverseStringAlternative(123456789))
print(reverseStringAlternative("Let's go to XYZ"))