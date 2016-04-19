from lib.data_structures.graphs.vertex import SimpleVertex


class SimpleGraph(object):

    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    def add_vertex(self, key):
        if key in self:
            return
        self.vertices[key] = SimpleVertex(key)
        self.vertex_count += 1

    def add_edge(self, vertex_a, vertex_b, undirected=True, weight=0):
        if vertex_a not in self.vertices:
            self.add_vertex(vertex_a)
        if vertex_b not in self.vertices:
            self.add_vertex(vertex_b)
        self.get_vertex(vertex_a).add_neighbor(self.get_vertex(vertex_b), weight)
        if undirected:
            self.get_vertex(vertex_b).add_neighbor(self.get_vertex(vertex_a), weight)

    def get_vertex(self, key):
        if key in self:
            return self.vertices[key]

    def get_vertices(self):
        return list(self.vertices.values())

    def clean_vertices(self):
        if self.vertex_count > 0:
            for v in self.get_vertices():
                v.color = "WHITE"
                v.distance = 0

    def __contains__(self, item):
        return item in self.vertices

    def __getitem__(self, item):
        return self.get_vertex(item)

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        items = []
        items.append("\nContents of graph_ds:")
        for item in self.vertices.values():
            items.append(str(item))
        return "\n".join(items)