from lib.data_structures.graphs.simple_graph import SimpleGraph


class DepthFirstSearchGraph(SimpleGraph):

    def dfs(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return

        start_vertex = self.get_vertex(start)
        end_vertex = self.get_vertex(end)
        self.clean_vertices()
        return self.__dfs_helper(start_vertex, end_vertex)

    def __dfs_helper(self, current, end):
        if current.get_id() == end.get_id():
            print("DFS: Found vertex '{0}' at a distance of {1} from start." .format(current.get_id(), current.distance))
            return True
        if current.get_connections():
            for neighbor in current.get_connections():
                if neighbor.color == "WHITE":
                    neighbor.color = "GRAY"
                    neighbor.distance = current.distance + 1
                    if self.__dfs_helper(neighbor, end):
                        return True
        current.color = "BLACK"

    def dfs_traverse(self):
        if self.vertexCount <= 0:
            return
        parents = {}
        for v in self.get_vertices():
            if v not in parents:
                parents[v] = None
                self.__traverse_helper(v, parents)
        return list(parents.keys())

    def __traverse_helper(self, startVertex, parents):
        for v in startVertex.get_connections():
            if v not in parents:
                parents[v] = startVertex
                self.__traverse_helper(v, parents)