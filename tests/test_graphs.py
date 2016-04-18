import unittest
from DataStructures.Graphs import Graph
from DataStructures.Graphs import BreadthFirstSearch
from DataStructures.Graphs import DepthFirstSearch
from DataStructures.Graphs import TopologicalSort
from DataStructures.Graphs import Dijkstra

class TestGraphs(unittest.TestCase):

    def buildGraph(self, graph, fileName, undirected):
        for line in open(fileName):
            elements = line.split()
            if len(elements) == 2:
                graph.addEdge(elements[0], elements[1], undirected)
            elif len(elements) == 3:
                graph.addEdge(elements[0], elements[1], undirected, elements[2])
        return graph

    def testGraphSimple(self):
        graph = Graph.SimpleGraph()
        graph = self.buildGraph(graph, "data/airport_routes.txt",True)

        self.assertEqual (graph.vertexCount, 10)

        for vert in graph:
            self.assertIsNotNone(vert)

        self.assertEqual(graph.getVertex("hey"), None)

        print(graph)

    def testBFS(self):
        graph = BreadthFirstSearch.BFSGraph()
        graph = self.buildGraph(graph, "data/airport_routes.txt", True)

        self.assertTrue(graph.breadthFirstSearch("DEN", "LAX"))
        self.assertIsNone(graph.breadthFirstSearch("Mark", "Steven"))
        self.assertIsNone(graph.breadthFirstSearch("LAX", "Steven"))

    def testDFS(self):
        graph = DepthFirstSearch.DFSGraph()
        graph = self.buildGraph(graph, "data/airport_routes.txt", True)

        self.assertTrue(graph.depthFirstSearch("LAX", "DFW"))
        self.assertIsNone(graph.depthFirstSearch("Mark", "Steven"))
        self.assertIsNone(graph.depthFirstSearch("LAX", "Steven"))

        self.assertEqual(len(graph.dfsTraverse()), graph.vertexCount)

    def testTopologicalSort(self):
        graph = TopologicalSort.TopologicalGraph()
        graph = self.buildGraph(graph, "data/execution_order_graph.txt", False)
        graph.topologicalSort()

    def testDijkstra(self):
        graph = Dijkstra.DijkstraGraph()
        graph = self.buildGraph(graph, "data/dijkstra_graph.txt", True)
        self.assertEqual(graph.dijkstra("z", "v"), ['z', 'y', 'x', 'v'])
        self.assertEqual(graph.dijkstra("u", "z"), ['u', 'x', 'y', 'z'])
        self.assertEqual(graph.dijkstra("w", "x"), ['w', 'y', 'x'])


