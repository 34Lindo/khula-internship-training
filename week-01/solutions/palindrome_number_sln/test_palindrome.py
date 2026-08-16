from solution import is_palindrome


def test_palindrome():
    assert is_palindrome(121) is True


def test_not_palindrome():
    assert is_palindrome(123) is False


def test_even_digit_palindrome():
    assert is_palindrome(1221) is True


def test_number_ending_zero():
    assert is_palindrome(10) is False


def test_negative_number():
    assert is_palindrome(-121) is False


def test_zero():
    assert is_palindrome(0) is True


def test_single_digit():
    assert is_palindrome(7) is True