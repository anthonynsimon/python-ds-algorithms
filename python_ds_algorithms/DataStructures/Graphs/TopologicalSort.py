from python_ds_algorithms.DataStructures.Graphs import Graph
from python_ds_algorithms.DataStructures import Queue

class TopologicalGraph(Graph.SimpleGraph):

    def topologicalSort(self):
        reverseOrderQueue = Queue.QueueLL()
        self.cleanVerticesHelpers()
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