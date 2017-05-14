from graph import Graph
import graph_functions
import unittest

__author__ = "hx8rc"

class TestGraphFuncs(unittest.TestCase):
    def test_is_complete_almost_complete(self):
        d = {}
        d["a"] = ["c","d"]
        d["b"] = ["c", "d"]
        d["c"] = ["b", "a", "d"]
        d["d"] = ["b", "c", "a"]
        g = Graph(d)
        self.assertEqual(graph_functions.is_complete(g), False)
    def test_is_complete(self):
        d = {}
        d["a"] = ["b", "c","d"]
        d["b"] = ["a","c", "d"]
        d["c"] = ["b", "a", "d"]
        d["d"] = ["b", "c", "a"]
        g = Graph(d)
        self.assertEqual(graph_functions.is_complete(g), True)
    def test_is_complete_empty(self):
        g = Graph()
        self.assertEqual(graph_functions.is_complete(g), True)
    def test_is_complete_nongraph(self):
        g = []
        self.assertRaises(TypeError, lambda: graph_functions.is_complete(g))
    def test_nodes_by_degree(self):
        d = {}
        d["a"] = ["b", "c", "d", "e"]
        d["b"] = ["a", "c"]
        d["c"] = ["a", "b", "d"]
        d["d"] = ["a", "c"]
        d["e"] = ["a"]
        g = Graph(d)
        self.assertIn(("a", 4), graph_functions.nodes_by_degree(g))
        self.assertIn(("c", 3), graph_functions.nodes_by_degree(g))
    def test_nodes_by_degree_empty(self):
        g = Graph()
        self.assertNotIn(("a", 4), graph_functions.nodes_by_degree(g))
        self.assertNotIn(("c", 3), graph_functions.nodes_by_degree(g))

