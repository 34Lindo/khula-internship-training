from solution import hammingWeight


def test_hamming_weight():
    assert hammingWeight(11) == 3
    assert hammingWeight(128) == 1
    assert hammingWeight(0) == 0
    assert hammingWeight((1 << 32) - 1) == 32


def test_one_bit():
    assert hammingWeight(1) == 1


def test_two_bits():
    assert hammingWeight(3) == 2


def test_no_bits():
    assert hammingWeight(0) == 0