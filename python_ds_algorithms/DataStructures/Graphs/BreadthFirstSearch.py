from python_ds_algorithms.DataStructures.Graphs import Graph
from python_ds_algorithms.DataStructures import Queue

class BFSGraph(Graph.SimpleGraph):

    def breadthFirstSearch(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return
        startVertex = self.getVertex(start)
        self.cleanVerticesHelpers()

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