from solution import isPalindrome

def test_valid_palindrome():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome("hello") == False
    print(" Yay!! All tests passed!")