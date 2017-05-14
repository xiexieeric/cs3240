__author__ = "hx8rc"

class Graph:
    def __init__(self, mydict = None):
        '''Initializes a new Graph with optional argument mydict as the adjacency list. If mydict is not provided,
        a blank Graph is created'''
        if mydict == None:
            self.dict = {}
        else:
            self.dict = mydict

    def __contains__(self, node):
        '''Returns true if the node is within the graph, false otherwise'''
        return node in self.dict.keys()

    def get_adjlist(self, node):
        '''Returns a list of nodes adjacent to node, returns None if node is not contained in the Graph'''
        if self.__contains__(node):
            return self.dict[node]
        else:
            return None

    def is_adjacent(self, node1, node2):
        '''Returns true if node1 is adjacent to node2, false otherwise'''
        if self.__contains__(node1):
            return node2 in self.dict[node1]
        else:
            return False

    def num_nodes(self):
        '''Returns the number of unique nodes in the graph'''
        return len(self.dict)

    def __str__(self):
        '''Returns a string representation of the adjacency list'''
        return self.dict.__str__()

    def __iter__(self):
        '''Returns an iterator through the adjacency list'''
        return iter(dict)

    def __len__(self):
        '''Returns the number of unique nodes in the graph'''
        return self.num_nodes()

    def add_node(self, node):
        '''Adds node to the graph if it is not already contained. Returns True if added successfully,
        False otherwise'''
        if self.__contains__(node):
            return False
        else:
            self.dict[node] = []
            return True
    def link_nodes(self, node1, node2):
        '''Creates an edge between node1 and node2 only if both are in the graph and not adjacent. Returns True
        if edge is created and false otherwise.'''
        if node1 == node2:
            return False
        if not self.__contains__(node1) or not self.__contains__(node2):
            return False
        if node2 in self.dict[node1] or node1 in self.dict[node2]:
            return False
        self.dict[node1].append(node2)
        self.dict[node2].append(node1)
        return True

    def unlink_nodes(self, node1, node2):
        '''Deletes the edge between node1 and node2 only if both are in the graph and adjacent. Returns True
        if edge is deleted and false otherwise.'''
        if node1 == node2:
            return False
        if not self.__contains__(node1) or not self.__contains__(node2):
            return False
        if node2 not in self.dict[node1] or node1 not in self.dict[node2]:
            return False
        self.dict[node1].remove(node2)
        self.dict[node2].remove(node1)
        return True

    def del_node(self, node):
        '''Deletes node and any connected edges from the graph only if it is contained already. Returns True if
        node was deleted successfully, False otherwise.'''
        if node in self.dict.keys():
            for neighbor in self.dict[node]:
                self.dict[neighbor].remove(node)
            self.dict.pop(node)
            return True
        else:
            return False

def main():
    print()
if __name__ == "__main__":
    main()