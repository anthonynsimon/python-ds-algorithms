from python_ds_algorithms.DataStructures.Graphs import Graph
from python_ds_algorithms.DataStructures.Trees import BinaryHeap
import sys

class DijkstraVertex(Graph.Vertex.SimpleVertex):

    def __init__(self, key):
        Graph.Vertex.SimpleVertex.__init__(self,key)
        self.predecessor = None

class DijkstraGraph(Graph.SimpleGraph):

    def addVertex(self, key):
        if key in self:
            return
        self.vertices[key] = DijkstraVertex(key)
        self.vertexCount += 1

    def dijkstra(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return

        self.cleanVerticesHelpers()

        startVertex = self.getVertex(start)
        endVertex = self.getVertex(end)

        for v in self.getVertices():
            v.distance = sys.maxsize
        startVertex.distance = 0

        pqheap = BinaryHeap.BinaryHeap()
        pqheap.buildHeap([(v.distance, v) for v in self.getVertices()])

        while pqheap.size() > 0:
            currentVertex = pqheap.deleteMin()
            currentVertex = currentVertex[1] # get the vertex from the tuple
            for neighbor in currentVertex.getConnections():
                newDistance = currentVertex.distance + currentVertex.getConnectionWeight(neighbor)
                if newDistance < neighbor.distance:
                    neighbor.distance = newDistance
                    neighbor.predecessor = currentVertex
                    pqheap.rebuildHeap()

        items = []
        traceVertex = endVertex
        done = False
        while not done:
            items.append(traceVertex.getID())
            if traceVertex.getID() == startVertex.getID():
                done = True
            traceVertex = traceVertex.predecessor
        items.reverse()
        print("\nResult from Dijkstra: {0}\n".format(" => ".join(items)))
        return items