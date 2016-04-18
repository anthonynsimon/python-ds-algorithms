from python_ds_algorithms.DataStructures.Graphs import Graph


class DFSGraph(Graph.SimpleGraph):

    def depthFirstSearch(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return

        startVertex = self.getVertex(start)
        endVertex = self.getVertex(end)
        self.cleanVerticesHelpers()
        return self.__depthFirstSearchWorker(startVertex, endVertex)

    def __depthFirstSearchWorker(self, currentVertex, endVertex):
        if currentVertex.getID() == endVertex.getID():
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
        if self.vertexCount <= 0:
            return
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