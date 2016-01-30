import unittest
from lib.data_structures.graphs.simple_graph import SimpleGraph
from lib.data_structures.graphs.breadth_first_search import BreathFirstSearchGraph
from lib.data_structures.graphs.depth_first_search import DepthFirstSearchGraph
from lib.data_structures.graphs.topological_sort import TopologicalGraph
from lib.data_structures.graphs.dijkstra import DijkstraGraph

class Testgraphs(unittest.TestCase):

    def build_graph(self, graph, fileName, undirected):
        for line in open(fileName):
            elements = line.split()
            if len(elements) == 2:
                graph.add_edge(elements[0], elements[1], undirected)
            elif len(elements) == 3:
                graph.add_edge(elements[0], elements[1], undirected, elements[2])
        return graph

    def test_simple_graph(self):
        my_graph = SimpleGraph()
        my_graph = self.build_graph(my_graph, "data/airport_routes.txt", True)

        self.assertEqual (my_graph.vertexCount, 10)

        for vert in my_graph:
            self.assertIsNotNone(vert)

        self.assertEqual(my_graph.get_vertex("hey"), None)

        print(my_graph)

    def testBFS(self):
        graph = BreathFirstSearchGraph()
        graph = self.build_graph(graph, "data/airport_routes.txt", True)

        self.assertTrue(graph.bfs("DEN", "LAX"))
        self.assertIsNone(graph.bfs("Mark", "Steven"))
        self.assertIsNone(graph.bfs("LAX", "Steven"))

    def testDFS(self):
        graph = DepthFirstSearchGraph()
        graph = self.build_graph(graph, "data/airport_routes.txt", True)

        self.assertTrue(graph.dfs("LAX", "DFW"))
        self.assertIsNone(graph.dfs("Mark", "Steven"))
        self.assertIsNone(graph.dfs("LAX", "Steven"))

        self.assertEqual(len(graph.dfs_traverse()), graph.vertexCount)

    def testTopological_sort(self):
        graph = TopologicalGraph()
        graph = self.build_graph(graph, "data/execution_order_graph.txt", False)
        graph.topological_sort()

    def testDijkstra(self):
        graph = DijkstraGraph()
        graph = self.build_graph(graph, "data/dijkstra_graph.txt", True)
        self.assertEqual(graph.dijkstra("z", "v"), ['z', 'y', 'x', 'v'])
        self.assertEqual(graph.dijkstra("u", "z"), ['u', 'x', 'y', 'z'])
        self.assertEqual(graph.dijkstra("w", "x"), ['w', 'y', 'x'])


