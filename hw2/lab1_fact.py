def factorial1(n):
    if(n<0):
        raise ValueError
    if n==0:
        return 1
    ret = 1
    for i in range(1,n+1):
        ret=ret*i
    return ret
def factorial2(n):
    ret = []
    for i in range(0,n+1):
        ret.append(factorial1(i))
    return ret
def test_fact1():
    assert factorial1(1) == 1
    assert factorial1(0) == 1
    assert factorial1(5) == 120
    try:
        factorial1(-5)
    except ValueError:
        print("We can't factorial a negative number")
if __name__ == "__main__":
    test_fact1()
    print(factorial2(5))
