from remove_duplicate import remove_duplicates

def test_remove_duplicates():
    # Empty list
    assert remove_duplicates([]) == []
    
    # No duplicates
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    
    # All duplicates
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    
    # Mixed duplicates
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    
    # Mixed types
    assert remove_duplicates([1, "1", 1, "1"]) == [1, "1"]
    
    # Strings
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    
    print("test_remove_duplicates: ALL PASSED")
    
test_remove_duplicates()