from lib.data_structures import Queue


def simulateHotPotato(namesList, numberOfPasses):
    simQueue = Queue.QueueLL()
    for name in namesList:
        simQueue.enqueue(name)

    for numberOfPeople in range (simQueue.size()):
        print("{0} {1}".format(simQueue.peek_head(), "has the potato!"))
        i = numberOfPasses
        while i > 0:
            simQueue.enqueue(simQueue.dequeue())
            print("{0} {1}".format("-> pass to", simQueue.peek_head()))
            i -= 1
        print("{0} {1}".format(simQueue.dequeue(), "is out!"))


people = ["Marcus", "Lucia", "John", "Max", "Sarah", "Sam"]
simulateHotPotato(people, 3)