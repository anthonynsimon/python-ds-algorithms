class SimpleVertex(object):

    def __init__(self, key):
        self.id = key
        self.color = ""
        self.distance = 0
        self.connections = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connections[neighbor] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_id(self):
        return self.id

    def get_connection_weight(self, neighbor):
        return int(self.connections[neighbor])

    def __repr__(self):
        return "vertex '{0}' ==> {1}".format(self.get_id(), [(x.id, self.get_connection_weight(x)) for x in self.connections])

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance
