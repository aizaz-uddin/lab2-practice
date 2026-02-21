from total_with_tax import total_with_tax

def test_total_with_tax():
    assert total_with_tax(100, 0.15) == 115
    assert total_with_tax(50, 0.1) == 55
    assert total_with_tax(0, 0.2) == 0
    assert total_with_tax(200, 0) == 200
    print("test_total_with_tax: ALL PASSED")
    
test_total_with_tax()