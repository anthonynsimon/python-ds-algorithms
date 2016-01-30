from lib.data_structures.graphs.simple_graph import SimpleGraph
from lib.data_structures.queue import QueueLL


class TopologicalGraph(SimpleGraph):

    def topological_sort(self):
        reverse_order_queue = QueueLL()
        self.clean_vertices()
        if self.vertexCount > 0:
            for v in self.get_vertices():
                if v.color == "WHITE":
                    self.__topo_sort_helper(v, reverse_order_queue)

            items = []
            while reverse_order_queue.size() > 0:
                items.insert(0, reverse_order_queue.dequeue())
            print("\nOrder of execution:")
            print(" -> ".join(x.get_id() for x in items))
            return items

    def __topo_sort_helper(self, currentVertex, queue):
        if currentVertex.color == "WHITE":
            if currentVertex.get_connections():
                for v in currentVertex.get_connections():
                    self.__topo_sort_helper(v, queue)
            currentVertex.color = "BLACK"
            queue.enqueue(currentVertex)