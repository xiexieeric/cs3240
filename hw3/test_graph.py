from graph import Graph
import unittest

__author__ = "hx8rc"

d = {}
d["a"] = ["b","c"]
d["b"] = ["a"]
d["c"] = ["a"]

class TestGraph(unittest.TestCase):
    def test_num_nodes_g1(self):
        """G1"""
        g = Graph(d)
        self.assertEqual(g.num_nodes(),3, "G1")


    def test_num_nodes_empty_g2(self):
        """G2"""
        g = Graph()
        self.assertEqual(g.num_nodes(),0, "G2")

    def test_dict_graph_does_contain_g3(self):
        """G3"""
        g = Graph(d)
        self.assertEqual(g.__contains__("a"),True,"G3")

    def test_dict_graph_not_contained_g4(self):
        """G4"""
        g = Graph(d)
        self.assertEqual(g.__contains__("d"),False,"G4")

    def test_adjlist_contained_g5(self):
        """G5"""
        g = Graph(d)
        self.assertEqual(g.get_adjlist("a"),d["a"],"G5")

    def test_adjlist_not_contained_g6(self):
        """G6"""
        g = Graph(d)
        self.assertEqual(g.get_adjlist("d"),None,"G6")

    def test_is_adjacent_g7(self):
        """G7"""
        g = Graph(d)
        self.assertEqual(g.is_adjacent("a", "b"),True,"G7")

    def test_not_adjacent_but_contained_g8(self):
        """G8"""
        g = Graph(d)
        self.assertEqual(g.is_adjacent("b", "c"),False,"G8")

    def test_not_adjacent_not_contained_g9(self):
        """G9"""
        g = Graph(d)
        self.assertEqual(g.is_adjacent("d","a"),False,"G9")


    def test_add_node_success_g10(self):
        """G10"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G10")
        self.assertEqual(g.num_nodes(),1,"G10")

    def test_add_node_fail_g11(self):
        """G11"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G11")
        self.assertEqual(g.num_nodes(),1, "G11")
        self.assertEqual(g.add_node("a"),False,"G11")
        self.assertEqual(g.__len__(),1, "G11")

    def test_link_nodes_success_g12(self):
        """G12"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G12")
        self.assertEqual(g.add_node("b"),True,"G12")
        self.assertEqual(g.link_nodes("a","b"),True,"G12")

    def test_link_nodes_same_nodes_g13(self):
        """G13"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G13")
        self.assertEqual(g.link_nodes("a","a"),False,"G13")


    def test_link_nodes_first_not_contained_g14(self):
        """G14"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G14")
        self.assertEqual(g.link_nodes("c","a"),False,"G14")

    def test_link_nodes_second_not_contained_g15(self):
        """G15"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G15")
        self.assertEqual(g.link_nodes("a","c"),False,"G15")

    def test_link_nodes_already_linked_g16(self):
        """G16"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G16")
        self.assertEqual(g.add_node("b"),True,"G16")
        self.assertEqual(g.link_nodes("a","b"),True,"G16")
        self.assertEqual(g.link_nodes("a", "b"),False,"G16")


    def test_unlink_nodes_success_g17(self):
        """G17"""
        g = Graph()
        self.assertEqual(g.dict,{})
        self.assertEqual(g.add_node("a"),True,"G17")
        self.assertEqual(g.add_node("b"),True,"G17")
        self.assertEqual(g.link_nodes("a","b"),True,"G17")
        self.assertEqual(g.unlink_nodes("b","a"),True,"G17")

    def test_unlink_nodes_same_nodes_g18(self):
        """G18"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G18")
        self.assertEqual(g.unlink_nodes("a","a"),False,"G18")


    def test_unlink_nodes_first_not_contained_g19(self):
        """G19"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G19")
        self.assertEqual(g.unlink_nodes("c","a"),False,"G19")

    def test_unlink_nodes_second_not_contained_g20(self):
        """G20"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G20")
        self.assertEqual(g.unlink_nodes("a","c"),False,"G20")

    def test_unlink_nodes_already_unlinked_g21(self):
        """G21"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G21")
        self.assertEqual(g.add_node("b"),True,"G21")
        self.assertEqual(g.unlink_nodes("a","b"),False,"G21")

    def test_del_node_success_g22(self):
        """G22"""
        g = Graph()
        self.assertEqual(g.dict,{})
        self.assertEqual(g.add_node("a"),True,"G22")
        self.assertEqual(g.add_node("b"),True,"G22")
        self.assertEqual(g.link_nodes("a","b"),True,"G22")
        self.assertEqual(g.is_adjacent("a","b"),True,"G22")
        self.assertEqual(g.del_node("a"),True,"G22")
        self.assertEqual(g.is_adjacent("a","b"),False,"G22")

    def test_del_node_not_contained_g23(self):
        """G23"""
        g = Graph()
        self.assertEqual(g.add_node("a"),True,"G23")
        self.assertEqual(g.del_node("b"),False,"G23")

