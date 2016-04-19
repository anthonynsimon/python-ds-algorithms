from lib.data_structures.graphs.simple_graph import SimpleGraph
from lib.data_structures.queue import QueueLL


class BreathFirstSearchGraph(SimpleGraph):

    def bfs(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return

        start_vertex = self.get_vertex(start)
        self.clean_vertices()

        queue = QueueLL()
        queue.enqueue(start_vertex)
        start_vertex.color = "GRAY"
        while queue.size() > 0:
            iteration_vertex = queue.dequeue()
            for neighbor in iteration_vertex.get_connections():
                if neighbor.color == "WHITE":
                    queue.enqueue(neighbor)
                    neighbor.color = "GRAY"
                    neighbor.distance = iteration_vertex.distance + 1
                if neighbor.get_id() == end:
                    print("BFS: Found vertex '{0}' at a distance of {1} from '{2}'" .format(neighbor.get_id(), neighbor.distance, start))
                    return True
            iteration_vertex.color = "BLACK"