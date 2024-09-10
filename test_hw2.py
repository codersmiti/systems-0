from hw2_debugging import merge_sort

def test_true1():
    arr = [3,5,1,2,4]
    assert merge_sort(arr)

def test_true2():
    arr1 = [2]
    assert merge_sort(arr1)

def test_true3():
    arr2 = [4,5,8]
    assert merge_sort(arr2)