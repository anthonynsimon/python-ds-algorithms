import random
from lib.data_structures.queue import QueueAA


class PrintTask(object):

    def __init__(self, pages):
        self.pages = pages

    def get_pages(self):
        return int(self.pages)

class Printer(object):

    def __init__(self, ppm):
        self.task_queue = QueueAA()
        self.__pages_per_minute = ppm
        self.__time_remaining = 0
        self.__current_task = None
        self.__waiting_times = []
        self.__job_history = {}
        self.__job_id = 1000

    def start_next_task(self):
        self.__current_task = self.task_queue.dequeue()
        if self.__current_task != None:
            #Task is starting
            print("Job #{0}: Starting new print task...".format(self.__job_id))
            self.__job_history[self.__job_id] = self.__current_task.get_pages()
            self.__time_remaining = self.__current_task.get_pages() * 60 / self.__pages_per_minute
            self.__waiting_times.append(self.__time_remaining)

    def tick(self):
        if self.__current_task != None:
            self.__time_remaining -= 1
            if self.__time_remaining <= 0:
                #Task is done
                print("Job #{0}: Task done. Printed {1} pages".format(self.__job_id, self.__job_history[self.__job_id]))
                self.__job_id += 1

        if self.__time_remaining <= 0:
            self.start_next_task()

    def add_print_task(self, task):
        self.task_queue.enqueue(task)

    def is_busy(self):
        return self.__current_task != None

    def average_waiting_time(self):
        return sum(self.__waiting_times) / len(self.__waiting_times)

    def average_pages(self):
        return sum(self.__job_history.values()) / len(self.__job_history)

    def reset_history(self):
        self.__waiting_times = []

    def reset_printing_queue(self):
        self.task_queue.clear()


class Simulation(object):

    def __init__(self, printer, number_of_students):
        self.printer = printer
        self.number_of_students = number_of_students

    def run(self, simulation_time):
        for i in range(self.number_of_students * 2):
            number_of_pages = random.randrange(1,21)
            self.printer.add_print_task(PrintTask(number_of_pages))

        for i in range(self.hours_to_seconds(simulation_time)):
            self.printer.tick()

    def hours_to_seconds(self, hours):
        return hours * 60 * 60


simulation = Simulation(Printer(5),10)
for i in range (10):
    simulation.run(1)
    print("The printer took an average of {0:0.1f} seconds to complete each task, "
          "average number of pages was {1} and {2} tasks remained"
          .format(simulation.printer.average_waiting_time(), int(simulation.printer.average_pages()),
                  simulation.printer.task_queue.size()))

    simulation.printer.reset_history()
    simulation.printer.reset_printing_queue()