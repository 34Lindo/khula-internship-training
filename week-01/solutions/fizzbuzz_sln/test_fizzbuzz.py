from solution import fizzbuzz

def test_fizzbuzz():
    result = fizzbuzz(15)

    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"

def test_number_not_divisible_by_3_or_5():
    result = fizzbuzz(7)

    assert result[6] == "7"


def test_divisible_by_3():
    result = fizzbuzz(81)

    assert result[80] == "Fizz"


def test_divisible_by_5():
    result = fizzbuzz(80)

    assert result[79] == "Buzz"


def test_divisible_by_both_3_and_5():
    result = fizzbuzz(225)

    assert result[224] == "FizzBuzz"
def test_zero():
    assert fizzbuzz(0) == []


def test_one():
    assert fizzbuzz(1) == ["1"]