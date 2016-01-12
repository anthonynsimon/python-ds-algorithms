class SimpleVertex(object):

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getConnectionWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __repr__(self):
        return "Vertex '{0}' ==> {1}".format(self.getID(), [x.id for x in self.connectedTo])
