from lib.data_structures.deque import Deque


def is_palindrome(data):
    deque = Deque()
    inputStr = str(data)
    result = True
    for character in inputStr:
        deque.add_head(character)

    # iterate over deque until either it proves false or
    # until there's only one character left (pivot point)
    while deque.size() > 1 and result == True:
        result = deque.remove_head() == deque.remote_tail()
        if not result:
            break
    return result


print(is_palindrome("radar"))
print(is_palindrome("hello"))