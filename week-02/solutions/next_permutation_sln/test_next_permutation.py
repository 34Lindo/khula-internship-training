from solution import nextPermutation


def test_next_permutation():
    nums = [1, 2, 3]
    nextPermutation(nums)
    assert nums == [1, 3, 2]


def test_descending_array():
    nums = [3, 2, 1]
    nextPermutation(nums)
    assert nums == [1, 2, 3]


def test_single_element():
    nums = [1]
    nextPermutation(nums)
    assert nums == [1]


def test_duplicate_values():
    nums = [1, 1, 5]
    nextPermutation(nums)
    assert nums == [1, 5, 1]


def test_middle_permutation():
    nums = [1, 3, 2]
    nextPermutation(nums)
    assert nums == [2, 1, 3]