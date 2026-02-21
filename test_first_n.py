from first_n import first_n

def test_first_n():
    assert first_n([10, 20, 30, 40], 3) == [10, 20, 30]

    assert first_n([1, 2, 3], 0) == []

    assert first_n([5, 6, 7], 1) == [5]

    assert first_n([1, 2, 3], 3) == [1, 2, 3]

    try:
        first_n([1, 2], 5)
        assert False, "Should have raised IndexError"
    except IndexError:
        pass

    print("test_first_n: ALL PASSED")
    
test_first_n()