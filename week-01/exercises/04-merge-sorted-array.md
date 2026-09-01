# Exercise 4: Merge Sorted Array

**Difficulty:** Easy
**Topics:** Arrays, Two-Pointer Technique
**Estimated Time:** 45-60 minutes

## Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of valid elements in `nums1` and `nums2` respectively.

**Merge `nums2` into `nums1` as one sorted array in-place.**

**Note:**

- You may assume that `nums1` has enough space to hold additional elements from `nums2` (i.e., `len(nums1) >= m + n`)
- You must modify `nums1` in-place (don't return a new array)

### Examples

**Input:**

```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
```

**Output:** `nums1 = [1,2,2,3,5,6]`
**Explanation:** Merged and sorted

**Input:**

```
nums1 = [1], m = 1
nums2 = [], n = 0
```

**Output:** `nums1 = [1]`

**Input:**

```
nums1 = [0], m = 0
nums2 = [1], n = 1
```

**Output:** `nums1 = [1]`

## Approach 1: Simple (O(m+n) space)

Merge into a new array, then copy back:

```
1. Create new array of size m+n
2. Compare elements from both arrays, add smaller one
3. Add remaining elements
4. Copy back to nums1
```

**Pros:** Easier to understand
**Cons:** Uses extra space (defeats the "in-place" goal)

## Approach 2: Two-Pointer from End (O(1) space) - RECOMMENDED

Start from the END of both arrays and work backwards:

```
1. Set pointer p to end of nums1 (m+n-1)
2. Set pointer i to end of valid elements in nums1 (m-1)
3. Set pointer j to end of nums2 (n-1)
4. While i >= 0 and j >= 0:
     - Compare nums1[i] and nums2[j]
     - Place larger element at nums1[p]
     - Move corresponding pointer backwards
5. If any elements remain in nums2, copy them
```

**Why backwards?** nums1 has empty space at the end! We can overwrite without losing data.

## Implementation

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place.

    Args:
        nums1: First sorted array with extra space
        m: Number of valid elements in nums1
        nums2: Second sorted array
        n: Number of valid elements in nums2

    Returns:
        None (modifies nums1 in-place)
    """
    # Your solution here
    pass
```

## Test Cases

```python
def test_merge():
    # Test 1: Basic merge
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Test 2: nums2 is empty
    nums1 = [1]
    nums2 = []
    merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

    # Test 3: nums1 is empty
    nums1 = [0]
    nums2 = [1]
    merge(nums1, 0, nums2, 1)
    assert nums1 == [1]

    # Test 4: All of nums2 smaller
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    # Test 5: All of nums2 larger
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    print("All tests passed!")

if __name__ == "__main__":
    test_merge()
```

## Learning Goals

By completing this exercise, you'll understand:

- The **two-pointer technique** - a fundamental algorithmic pattern
- How to work backwards to avoid overwriting data
- In-place modifications and space efficiency
- Why problem constraints matter (nums1 has extra space!)

## Complexity Analysis

**Approach 1 (With Extra Space):**

- Time Complexity: O(m + n) - merge all elements
- Space Complexity: O(m + n) - new array

**Approach 2 (Two-Pointer from End) - Recommended:**

- Time Complexity: O(m + n) - single pass
- Space Complexity: O(1) - in-place, no extra space

## Key Insights

1. **Two-pointer technique:** Compare two sorted sequences by advancing pointers
2. **Backward processing:** When extra space is at the END, process from back to front
3. **Space efficiency:** The problem gives us exactly the space we need
4. **Merging sorted data:** Core operation in merge sort and other algorithms

## Visualization

```
nums1 = [1,2,3,0,0,0]   nums2 = [2,5,6]
           ↑                      ↑
         i=2                    j=2
                           p=5

Step 1: Compare nums1[2]=3 and nums2[2]=6
        6 is larger, place at nums1[5]=6
        Move j backward

Step 2: Compare nums1[2]=3 and nums2[1]=5
        5 is larger, place at nums1[4]=5
        Move j backward

Step 3: Compare nums1[2]=3 and nums2[0]=2
        3 is larger, place at nums1[3]=3
        Move i backward

Continue...
```

## Edge Cases

- One array is empty
- Arrays have different lengths
- All elements of nums2 are smaller/larger than nums1
- Duplicate elements
- Single element arrays

## Follow-up Questions

1. Why is the backward approach better than merging forward?
2. What if you weren't allowed to modify nums1?
3. How would this change for descending order?
4. Can you implement merge sort using this technique?

## Mentor Notes

Common mistakes:

- Forgetting to handle remaining elements in nums2
- Moving the wrong pointer after comparison
- Overwriting data because they're processing forward instead of backward

Teaching moments:

- Emphasize why backward processing matters here
- Compare Approach 1 vs 2: which is more elegant?
- Discuss real-world scenarios (memory-constrained systems)
- Foreshadow merge sort (which uses similar merge logic)
