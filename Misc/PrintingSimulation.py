import random
from DataStructures import Queue


class PrintTask(object):

    def __init__(self, pages):
        self.pages = pages

    def getPages(self):
        return int(self.pages)

class Printer(object):

    def __init__(self, ppm):
        self.__pagesPerMinute = ppm
        self.__timeRemaining = 0
        self.__currentTask = None
        self.taskQueue = Queue.QueueAA()
        self.__waitingTimes = []
        self.__jobHistory = {}
        self.__jobID = 1000

    def startNextTask(self):
        self.__currentTask = self.taskQueue.dequeue()
        if self.__currentTask != None:
            #Task is starting
            print("Job #{0}: Starting new print task...".format(self.__jobID))
            self.__jobHistory[self.__jobID] = self.__currentTask.getPages()
            self.__timeRemaining = self.__currentTask.getPages() * 60 / self.__pagesPerMinute
            self.__waitingTimes.append(self.__timeRemaining)

    def tick(self):
        if self.__currentTask != None:
            self.__timeRemaining -= 1
            if self.__timeRemaining <= 0:
                #Task is done
                print("Job #{0}: Task done. Printed {1} pages".format(self.__jobID, self.__jobHistory[self.__jobID]))
                self.__jobID += 1

        if self.__timeRemaining <= 0:
            self.startNextTask()

    def addPrintTask(self, task):
        self.taskQueue.enqueue(task)

    def isBusy(self):
        return self.__currentTask != None

    def averageWaitingTime(self):
        return sum(self.__waitingTimes) / len(self.__waitingTimes)

    def averagePages(self):
        return sum(self.__jobHistory.values()) / len(self.__jobHistory)

    def resetHistory(self):
        self.__waitingTimes = []

    def resetPrintQueue(self):
        self.taskQueue.clear()

class Simulation(object):

    def __init__(self, printer, numberOfStudents):
        self.printer = printer
        self.numberOfStudents = numberOfStudents

    def run(self, timeToSimulate):
        for i in range(self.numberOfStudents * 2):
            numberOfPages = random.randrange(1,21)
            self.printer.addPrintTask(PrintTask(numberOfPages))

        for i in range(self.hoursToSeconds(timeToSimulate)):
            self.printer.tick()

    def hoursToSeconds(self, hours):
        return hours * 60 * 60


simulation = Simulation(Printer(5),10)
for i in range (10):
    simulation.run(1)
    print("The printer took an average of {0:0.1f} seconds to complete each task, "
          "average number of pages was {1} and {2} tasks remained"
          .format(simulation.printer.averageWaitingTime(), int(simulation.printer.averagePages()),
                  simulation.printer.taskQueue.size()))

    simulation.printer.resetHistory()
    simulation.printer.resetPrintQueue()