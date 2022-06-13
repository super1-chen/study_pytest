import bisect
from bisect_example import bisect_right, bisect_left

array = [1,1,2,2,2,3,4]

def test_bisect_left_ok():
    # 2 a[0:i] < x 
    assert bisect_left(array, 2) == 2
    
def test_bisect_right_ok():
    # a[i::] > a[x]
    assert bisect_right(array, 2) == 5
    
