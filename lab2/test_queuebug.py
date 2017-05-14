__author__ = 'Eric Xie'

from ourqueue import OurQueue

def test_init_bug():
    """ test the init function for bugs"""
    myArr = [1,2,3]
    q1 = OurQueue(myArr)
    myArr[0]= -1
    res = q1.front()
    assert res == -1
