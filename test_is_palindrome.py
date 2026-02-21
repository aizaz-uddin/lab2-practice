from is_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("madam") == True
    
    assert is_palindrome("hello") == False
    
    assert is_palindrome("nurses run") == True
    
    assert is_palindrome("") == True
    
    assert is_palindrome("a") == True
    
    assert is_palindrome("Madam") == False
    
    print("test_is_palindrome: ALL PASSED")
    
test_is_palindrome()