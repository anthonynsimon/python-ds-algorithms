import Queue

def simulateHotPotato(namesList, number):
    simQueue = Queue.LLQueue()

    for name in namesList:
        simQueue.enqueue(name)

    for numberOfPeople in range (simQueue.size()):
        i = number
        while i > 0:
            print("-> pass to", simQueue.peek())
            simQueue.enqueue(simQueue.dequeue())
            i -= 1

        print(simQueue.dequeue(), "is out!")

    print(simQueue.peek())

people = ["Marcus", "Lucia", "John", "Max", "Sarah", "Sam"]
simulateHotPotato(people, 3)