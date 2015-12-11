import random
from DataStructures import Queue


class PrintTask(object):

    def __init__(self, pages):
        self.pages = pages

    def getPages(self):
        return int(self.pages)

class Printer(object):

    def __init__(self, ppm):
        self.pagesPerMinute = ppm
        self.timeRemaining = 0
        self.currentTask = None
        self.taskQueue = Queue.QueueAA()
        self.waitingTimes = []
        self.jobHistory = {}
        self.jobID = 1000

    def startNextTask(self):
        self.currentTask = self.taskQueue.dequeue()
        if self.currentTask != None:
            #Task is starting
            print("Job #{0}: Starting new print task...".format(self.jobID))
            self.jobHistory[self.jobID] = self.currentTask.getPages()
            self.timeRemaining = self.currentTask.getPages() * 60/self.pagesPerMinute
            self.waitingTimes.append(self.timeRemaining)

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                #Task is done
                print("Job #{0}: Task done. Printed {1} pages".format(self.jobID, self.jobHistory[self.jobID]))
                self.jobID += 1

        if self.timeRemaining <= 0:
            self.startNextTask()

    def addPrintTask(self, task):
        self.taskQueue.enqueue(task)

    def isBusy(self):
        return self.currentTask != None

    def averageWaitingTime(self):
        return sum(self.waitingTimes)/len(self.waitingTimes)

    def averagePages(self):
        return sum(self.jobHistory.values())/len(self.jobHistory)

    def resetHistory(self):
        self.waitingTimes = []

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