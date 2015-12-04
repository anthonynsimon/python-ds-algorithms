from DataStructures import Queue

def simulateHotPotato(namesList, numberOfPasses):
    simQueue = Queue.LLQueue()

    for name in namesList:
        simQueue.enqueue(name)

    for numberOfPeople in range (simQueue.size()):
        print("{0} {1}".format(simQueue.peek(), "has the potato!"))
        i = numberOfPasses
        while i > 0:
            simQueue.enqueue(simQueue.dequeue())
            print("{0} {1}".format("-> pass to", simQueue.peek()))
            i -= 1

        print("{0} {1}".format(simQueue.dequeue(), "is out!"))

people = ["Marcus", "Lucia", "John", "Max", "Sarah", "Sam"]
simulateHotPotato(people, 3)