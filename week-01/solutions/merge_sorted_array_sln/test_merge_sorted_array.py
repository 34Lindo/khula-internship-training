from solution import merge


def test_basic_merge():
    nums1 = [1, 2, 3, 0, 0, 0]

    merge(nums1, 3, [2, 5, 6], 3)

    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_empty_second_array():
    nums1 = [1]

    merge(nums1, 1, [], 0)

    assert nums1 == [1]


def test_empty_first_array():
    nums1 = [0]

    merge(nums1, 0, [1], 1)

    assert nums1 == [1]


def test_second_array_values_are_smaller():
    nums1 = [4, 5, 6, 0, 0, 0]

    merge(nums1, 3, [1, 2, 3], 3)

    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_duplicate_values():
    nums1 = [1, 2, 2, 0, 0, 0]

    merge(nums1, 3, [2, 2, 3], 3)

    assert nums1 == [1, 2, 2, 2, 2, 3]


def test_single_elements():
    nums1 = [2, 0]

    merge(nums1, 1, [1], 1)

    assert nums1 == [1, 2]