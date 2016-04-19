from lib.data_structures.deque import Deque


def reverse_string(string):
    deque = Deque()
    input_string = str(string)
    items = []
    for ch in input_string:
        deque.add_head(ch)
    for i in range(deque.size()):
        items.append(deque.remove_head())
    return "".join(items)

def reverse_string_v2(string):
    input = str(string)
    length = len(input)
    items = []
    for i in range(length):
        items.append(input[length - 1 - i])
    return "".join(items)


text = "Let's grab some lunch"
print(text)
text = reverse_string(text)
print(text)
text = reverse_string_v2(text)
print(text)
print(reverse_string_v2(123456789))
print(reverse_string("Let's go to XYZ"))