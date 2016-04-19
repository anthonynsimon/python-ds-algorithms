from lib.data_structures.queue import QueueLL


def simulate_hot_potato(names, number_of_passes):
    queue = QueueLL()
    for name in names:
        queue.enqueue(name)

    for numberOfPeople in range (queue.size()):
        print("{0} {1}".format(queue.peek(), "has the potato!"))
        i = number_of_passes
        while i > 0:
            queue.enqueue(queue.dequeue())
            print("{0} {1}".format("-> pass to", queue.peek()))
            i -= 1
        print("{0} {1}".format(queue.dequeue(), "is out!"))


people = ["Marcus", "Lucia", "John", "Max", "Sarah", "Sam"]
simulate_hot_potato(people, 3)