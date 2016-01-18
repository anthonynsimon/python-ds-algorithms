from DataStructures.Graphs import Vertex

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

    def cleanVerticesHelpers(self):
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