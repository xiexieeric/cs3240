#Eric Xie hx8rc
def maxIndex(list):
    if not len(list)==0:
        ret = 0
        for i in range(len(list)):
            if list[i] > list[ret]:
                ret=i
        return ret
def minIndex(list):
    if not len(list)==0:
        ret = 0
        for i in range(len(list)):
            if list[i] < list[ret]:
                ret=i
        return ret
def maxmin(list):
    """Return a tuple where the first value is the maximum value found in the list and the second
    value in the tuple is the minimum value found in the list (based on the < operator)."""
    if len(list)==0:
        return None
    myMax = list[maxIndex(list)]
    myMin = list[minIndex(list)]
    return (myMax,myMin)
def common_items(list1, list2):
    """Return a list that contains items that are found in both lists."""
    ret = []
    for item in list1:
        if item in list2 and item not in ret:
            ret.append(item)
    return ret
def notcommon_items(list1, list2):
    """Return a list that contains items that only occur in one of list1 or list2 (i.e. not in both lists)."""
    ret = []
    for item in list1:
        if item not in list2 and item not in ret:
            ret.append(item)
    for item in list2:
        if item not in list1 and item not in ret:
            ret.append(item)
    return ret
def count_list_items(list):
    """Return a dictionary that stores counts of how often each item occurs."""
    ret = {}
    for item in list:
        if item in ret.keys():
            ret[item] += 1
        else:
            ret[item] = 1
    return ret
def test_func():
    assert maxmin(['Q', 'Z', 'C', 'A'],) == ('Z','A')
    assert maxmin([3, 1, -2]) == (3,-2)
    assert maxmin([1,4,5,6,35,102,-2]) == (102,-2)
    assert maxmin(['Q', 'Z', 'C', 'A']) == ('Z','A')
    assert common_items([1,2,3,4,5,5],[4,5,6,7,8]) == [4,5]
    print(count_list_items([1, 3, 2, 2, 3, 1, 1, 2]))
if __name__ == "__main__":
    test_func()
