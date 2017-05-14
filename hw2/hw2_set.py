#Eric Xie hx8rc
class OurSet:
    """
    OurSet is a class that represents an unordered Set in discrete math. It supports the addition of individual objects,
    and the addition of a list of objects, but cannot remove objects. It is iterable and can be used to perform set union
    and set intersection with other objects of type OurSet, returning the result as an OurSet.
    """
    def __init__(self):
        """Initializes an empty set."""
        self.myList = []

    def add(self, item):
        """If the parameter to this method is not already in the set object, add it to the set. Return True or False to
        indicate if the item was added to the set.
        """
        if item in self.myList:
            return False
        else:
            self.myList.append(item)
            return True

    def add_list(self, list):
        """Add each item in the list to the set, unless it already is in the set. Return True if any item was added the
set, otherwise False."""
        itemAdded = False
        for item in list:
            if item not in self.myList:
                self.myList.append(item)
                itemAdded = True
        return itemAdded

    def __str__(self):
        """Return a string representation of the set of format "<a, b, c>" where a, b, and c are members of the set."""
        if len(self.myList)== 0:
            return "<>"
        ret = "<"
        for item in self.myList:
            ret += str(item) + ", "
        ret = ret[:-2] + ">"
        return ret

    def __len__(self):
        """Returns the number of items in the set object."""
        return len(self.myList)

    def __iter__(self):
        """Returns an iterator for the items in the list."""
        return iter(self.myList)

    def union(self, set2):
        """Returns the set-union of this set with set2."""
        ret = OurSet()
        for item in self.myList:
            if item not in ret:
                ret.add(item)
        for item in set2:
            if item not in ret:
                ret.add(item)
        return ret

    def intersection(self, set2):
        """Returns the set-intersection of this set with set2."""
        ret = OurSet()
        for item in self.myList:
            if item in set2 and item not in ret:
                ret.add(item)
        return ret


def test():
    s1 = OurSet()
    s2 = OurSet()
    s3 = s1.union(s2)
    print(s2.add_list([4, 5, 6, 7, 8]))
    s4 = s3.union(s2)
    s4.add(3)
    print(s4)
    print(s1.add_list([1, 2, 3, 4, 5, 5]))
    print(s2.add_list([4, 5, 6, 7, 8]))
    print(s1.intersection(s2))
    print(s1.union(s2))
    print(s1.intersection(s3))
if __name__ == "__main__":
    test()
