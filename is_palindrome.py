def is_palindrome(s):
    cleaned = s.replace(" ", "")
    return cleaned == cleaned[::-1]
