from graph import Graph

__author__ = "hx8rc"

def is_complete(grph):
    """Returns True if grph is a complete Graph. That is, if every node in grph is connected to every
    other node. Returns False otherwise."""
    ret = True
    if isinstance(grph,Graph):
        g = grph
    else:
        raise TypeError("Not a Graph object")
    if g.num_nodes() == 0 or g.num_nodes() == 1:
        return ret
    for node in g.dict.keys():
        for neighbor in g.dict.keys():
            if not g.is_adjacent(node,neighbor) and node != neighbor:
                ret = False
    return ret

def nodes_by_degree(grph):
    """Returns a list of tuples containing each node and its degree, the number of edges connected to the
    node. The tuples are listed in descending degree."""
    if isinstance(grph,Graph):
        g = grph
    else:
        raise TypeError("Not a Graph object")
    ret = []
    for node in g.dict:
        temp = (node,len(g.get_adjlist(node)))
        ret.append(temp)
    ret.sort(key = lambda tup: tup[1], reverse=True)
    return ret

if __name__ == "__main__":
    print()

