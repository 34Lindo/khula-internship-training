from solution import reverseBits


def test_reverse_bits():
    assert reverseBits(43261596) == 964176192
    assert reverseBits(1) == 2147483648


def test_zero():
    assert reverseBits(0) == 0


def test_max_32_bit_integer():
    assert reverseBits(4294967295) == 4294967295