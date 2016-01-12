from DataStructures.Graphs import Vertex
from DataStructures import Queue

class SimpleGraph(object):

    def __init__(self):
        self.vertices = {}
        self.vertexCount = 0

    def addVertex(self, key):
        if key in self:
            return
        self.vertices[key] = Vertex.SimpleVertex(key)
        self.vertexCount += 1

    def addEdge(self, vertexA, vertexB, weight=0):
        if vertexA not in self.vertices:
            self.addVertex(vertexA)
        if vertexB not in self.vertices:
            self.addVertex(vertexB)
        self.getVertex(vertexA).addNeighbor(self.getVertex(vertexB), weight)
        self.getVertex(vertexB).addNeighbor(self.getVertex(vertexA), weight)

    def getVertex(self, key):
        if key in self:
            return self.vertices[key]

    def getVertices(self):
        return list(self.vertices.values())

    def depthFirstSearch(self, start, end):
        vertices = self.getVertices()
        if vertices:
            startVertex = self.getVertex(start)
            if startVertex is None:
                return

            distance = 0
            colored = {}
            queue = Queue.QueueLL()

            for v in vertices:
                colored[v] = "WHITE"

            queue.enqueue(self.getVertex(start))
            colored[self.getVertex(start)] = "GRAY"

            while queue.size() > 0:
                iterationVertex = queue.dequeue()
                distance += 1
                for neighbor in iterationVertex.getConnections():
                    if neighbor.getID() == end:
                        print("Found vertex '{0}' at a distance of {1} from '{2}'" .format(neighbor.getID(), distance, start))
                        return distance
                    if colored[neighbor] == "WHITE":
                        queue.enqueue(neighbor)
                        colored[neighbor] = "GRAY"
                colored[iterationVertex] = "BLACK"

    def __contains__(self, item):
        return item in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        items = []
        items.append("\nContents of Graph:")
        for item in self.vertices.values():
            items.append(str(item))
        return "\n".join(items)