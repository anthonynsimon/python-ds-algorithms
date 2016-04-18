from python_ds_algorithms.DataStructures import Deque


def isPalindrome(string):
    deque = Deque.Deque()
    inputStr = str(string)
    result = True
    for character in inputStr:
        deque.addHead(character)

    # iterate over deque until either it proves false or
    # until there's only one character left (pivot point)
    while deque.size() > 1 and result == True:
        result = deque.removeHead() == deque.removeTail()
        if result == False:
            break
    return result


print(isPalindrome("radar"))
print(isPalindrome("hello"))