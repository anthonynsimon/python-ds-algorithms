from lib.data_structures.graphs.simple_graph import SimpleGraph
from lib.data_structures.graphs.vertex import SimpleVertex
from lib.data_structures.trees.binary_heap import BinaryHeap
import sys


class DijkstraVertex(SimpleVertex):

    def __init__(self, key):
        SimpleVertex.__init__(self,key)
        self.predecessor = None

class DijkstraGraph(SimpleGraph):

    def add_vertex(self, key):
        if key in self:
            return
        self.vertices[key] = DijkstraVertex(key)
        self.vertex_count += 1

    def dijkstra(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return

        self.clean_vertices()

        start_vertex = self.get_vertex(start)
        end_vertex = self.get_vertex(end)

        for v in self.get_vertices():
            v.distance = sys.maxsize
        start_vertex.distance = 0

        pq = BinaryHeap()
        pq.build_heap([(v.distance, v) for v in self.get_vertices()])

        while pq.size() > 0:
            current = pq.delete_min()
            current = current[1] # get the vertex from the tuple
            for neighbor in current.get_connections():
                new_distance = current.distance + current.get_connection_weight(neighbor)
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.predecessor = current
                    pq.rebuild_heap()

        items = []
        trace_vertex = end_vertex
        done = False
        while not done:
            items.append(trace_vertex.get_id())
            if trace_vertex.get_id() == start_vertex.get_id():
                done = True
            trace_vertex = trace_vertex.predecessor
        items.reverse()
        print("\nResult from dijkstra: {0}\n".format(" => ".join(items)))
        return items