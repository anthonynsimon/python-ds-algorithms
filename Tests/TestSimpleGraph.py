import unittest
from DataStructures.Graphs import Graph


class TestSimpleGraph(unittest.TestCase):

    def testGraph(self):
        graph = Graph.SimpleGraph()
        for line in open("AirportRoutes.txt"):
            elements = line.split()
            if len(elements) == 2:
                graph.addEdge(elements[0], elements[1])

        self.assertEqual (graph.vertexCount, 10)

        for vert in graph:
            self.assertIsNotNone(vert)

        self.assertEqual(graph.getVertex("hey"), None)

        print(graph)

        self.assertIn(graph.depthFirstSearch("LAX", "DFW"), [2,3])
        self.assertEqual(graph.depthFirstSearch("Mark", "Steven"), None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleGraph)
unittest.TextTestRunner(verbosity=2).run(suite)