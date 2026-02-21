from max_of_three import max_of_three

def test_max_of_three():
    assert max_of_three(2,5,9) == 9
    assert max_of_three(-5,-8,-19) == -5
    assert max_of_three(2,0,1) == 2
    assert max_of_three(3,3,1) ==3
    assert max_of_three(9,9,9) == 9
    
    print("test_max_of_three: ALL PASSED")
    
test_max_of_three()