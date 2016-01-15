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

    def addEdge(self, vertexA, vertexB, undirected=True, weight=0):
        if vertexA not in self.vertices:
            self.addVertex(vertexA)
        if vertexB not in self.vertices:
            self.addVertex(vertexB)
        self.getVertex(vertexA).addNeighbor(self.getVertex(vertexB), weight)
        if undirected:
            self.getVertex(vertexB).addNeighbor(self.getVertex(vertexA), weight)

    def getVertex(self, key):
        if key in self:
            return self.vertices[key]

    def getVertices(self):
        return list(self.vertices.values())

    def breathFirstSearch(self, start, end):
        vertices = self.getVertices()
        if vertices:
            startVertex = self.getVertex(start)
            if startVertex is None:
                return
            self.__cleanVerticesHelpers()

            queue = Queue.QueueLL()
            queue.enqueue(startVertex)
            startVertex.v = "GRAY"
            while queue.size() > 0:
                iterationVertex = queue.dequeue()
                for neighbor in iterationVertex.getConnections():
                    if neighbor.color == "WHITE":
                        queue.enqueue(neighbor)
                        neighbor.color = "GRAY"
                        neighbor.distance = iterationVertex.distance + 1
                    if neighbor.getID() == end:
                        print("BFS: Found vertex '{0}' at a distance of {1} from '{2}'" .format(neighbor.getID(), neighbor.distance, start))
                        return True
                iterationVertex.color = "BLACK"

    def depthFirstSearch(self, startVertex, endVertex):
        vertices = self.getVertices()
        if vertices:
            startVertex = self.getVertex(startVertex)
            if startVertex is None:
                return
            self.__cleanVerticesHelpers()
            return self.__depthFirstSearchWorker(startVertex, endVertex)

    def __depthFirstSearchWorker(self, currentVertex, endVertex):
        if currentVertex.getID() == endVertex:
            print("DFS: Found vertex '{0}' at a distance of {1} from start." .format(currentVertex.getID(), currentVertex.distance))
            return True
        if currentVertex.getConnections():
            for neighbor in currentVertex.getConnections():
                if neighbor.color == "WHITE":
                    neighbor.color = "GRAY"
                    neighbor.distance = currentVertex.distance + 1
                    if self.__depthFirstSearchWorker(neighbor, endVertex):
                        return True
        currentVertex.color = "BLACK"

    def dfsTraverse(self):
        parents = {}
        for v in self.getVertices():
            if v not in parents:
                parents[v] = None
                self.__dfsTraverseWorker(v, parents)
        return list(parents.keys())

    def __dfsTraverseWorker(self, startVertex, parents):
        for v in startVertex.getConnections():
            if v not in parents:
                parents[v] = startVertex
                self.__dfsTraverseWorker(v, parents)

    def topologicalSort(self):
        reverseOrderQueue = Queue.QueueLL()
        self.__cleanVerticesHelpers()
        if self.vertexCount > 0:
            for v in self.getVertices():
                if v.color == "WHITE":
                    self.__topologicalSortHelper(v,reverseOrderQueue)

        items = []
        while reverseOrderQueue.size() > 0:
            items.insert(0, reverseOrderQueue.dequeue())
        print("\nOrder of execution:")
        print(" -> ".join(x.getID() for x in items))
        return items

    def __topologicalSortHelper(self, currentVertex, queue):
        if currentVertex.color == "WHITE":
            if currentVertex.getConnections():
                for v in currentVertex.getConnections():
                    self.__topologicalSortHelper(v, queue)
            currentVertex.color = "BLACK"
            queue.enqueue(currentVertex)

    def __cleanVerticesHelpers(self):
        if self.vertexCount > 0:
            for v in self.getVertices():
                v.color = "WHITE"
                v.distance = 0

    def __contains__(self, item):
        return item in self.vertices

    def __getitem__(self, item):
        return self.getVertex(item)

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        items = []
        items.append("\nContents of Graph:")
        for item in self.vertices.values():
            items.append(str(item))
        return "\n".join(items)