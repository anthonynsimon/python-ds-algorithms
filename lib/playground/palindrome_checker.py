from lib.data_structures import deque


def is_palindrome(data):
    _deque = deque.Deque()
    inputStr = str(data)
    result = True
    for character in inputStr:
        _deque.add_head(character)

    # iterate over deque until either it proves false or
    # until there's only one character left (pivot point)
    while _deque.size() > 1 and result == True:
        result = _deque.remove_head() == _deque.remote_tail()
        if result == False:
            break
    return result


print(is_palindrome("radar"))
print(is_palindrome("hello"))