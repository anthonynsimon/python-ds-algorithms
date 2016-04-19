from lib.data_structures.graphs.simple_graph import SimpleGraph
from lib.data_structures.queue import QueueLL


class TopologicalGraph(SimpleGraph):

    def topological_sort(self):
        reverse_order_queue = QueueLL()
        self.clean_vertices()
        if self.vertex_count > 0:
            for v in self.get_vertices():
                if v.color == "WHITE":
                    self.__topo_sort_helper(v, reverse_order_queue)

            items = []
            while reverse_order_queue.size() > 0:
                items.insert(0, reverse_order_queue.dequeue())
            print("\nOrder of execution:")
            print(" -> ".join(x.get_id() for x in items))
            return items

    def __topo_sort_helper(self, current_vertex, queue):
        if current_vertex.color == "WHITE":
            if current_vertex.get_connections():
                for v in current_vertex.get_connections():
                    self.__topo_sort_helper(v, queue)
            current_vertex.color = "BLACK"
            queue.enqueue(current_vertex)