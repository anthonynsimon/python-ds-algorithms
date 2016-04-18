class SimpleVertex(object):

    def __init__(self, key):
        self.id = key
        self.color = ""
        self.distance = 0
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getConnectionWeight(self, neighbor):
        return int(self.connectedTo[neighbor])

    def __repr__(self):
        #return self.getID()
        return "Vertex '{0}' ==> {1}".format(self.getID(), [(x.id, self.getConnectionWeight(x)) for x in self.connectedTo])

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance
