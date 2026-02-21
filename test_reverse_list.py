from reverse_list import reverse_list

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    
    assert reverse_list([10]) == [10]
    
    assert reverse_list([]) == []
    
    assert reverse_list([1, 2, 2, 1]) == [1, 2, 2, 1]
    
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']

    print("test_reverse_list: ALL PASSED")


test_reverse_list()