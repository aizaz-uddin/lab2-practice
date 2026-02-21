from find_min import find_min

def test_find_min():
    assert find_min([3, 1, 4, 2]) == 1
    
    assert find_min([5, 7, 9, 2]) == 2
    
    assert find_min([-1, -5, -3]) == -5
    
    assert find_min([10]) == 10
    
    assert find_min([-2, 5, 0, 3]) == -2
    
    assert find_min([100, 50, 75]) == 50
    
    print("test_find_min: ALL PASSED")
    
test_find_min()