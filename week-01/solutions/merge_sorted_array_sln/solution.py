def merge(
    nums1: list[int],
    m: int,
    nums2: list[int],
    n: int
) -> None:
    """
    Merge nums2 into nums1 in sorted order.

    The merge is performed in-place.

    Args:
        nums1: First sorted list with enough space for nums2.
        m: Number of actual elements in nums1.
        nums2: Second sorted list.
        n: Number of elements in nums2.

    Returns:
        None
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1