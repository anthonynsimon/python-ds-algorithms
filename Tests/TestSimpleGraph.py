import unittest
from DataStructures.Graphs import Graph


class TestSimpleGraph(unittest.TestCase):

    def buildGraph(self, fileName, undirected):
        graph = Graph.SimpleGraph()
        for line in open(fileName):
            elements = line.split()
            if len(elements) == 2:
                graph.addEdge(elements[0], elements[1], undirected)
            elif len(elements) == 3:
                graph.addEdge(elements[0], elements[1], undirected, elements[2])
        return graph

    def testGraphSimple(self):
        graph = self.buildGraph("AirportRoutes.txt",True)

        self.assertEqual (graph.vertexCount, 10)

        for vert in graph:
            self.assertIsNotNone(vert)

        self.assertEqual(graph.getVertex("hey"), None)

        print(graph)

    def testTraversals(self):
        graph = self.buildGraph("AirportRoutes.txt",True)

        self.assertTrue(graph.breathFirstSearch("DEN", "LAX"))
        self.assertIsNone(graph.breathFirstSearch("Mark", "Steven"))
        self.assertIsNone(graph.breathFirstSearch("LAX", "Steven"))

        self.assertTrue(graph.depthFirstSearch("LAX", "DFW"))
        self.assertIsNone(graph.depthFirstSearch("Mark", "Steven"))
        self.assertIsNone(graph.depthFirstSearch("LAX", "Steven"))

        self.assertEqual(len(graph.dfsTraverse()), graph.vertexCount)

    def testTopologicalSort(self):
        graph = self.buildGraph("ExecutionOrderGraph.txt",False)
        graph.topologicalSort()

    # def testDijkstra(self):
    #     graph = self.buildGraph("GraphForDijkstra.txt",True)
    #     graph.dijkstra("u", "z")


suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleGraph)
unittest.TextTestRunner(verbosity=2).run(suite)