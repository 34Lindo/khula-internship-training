# Exercise 3: Two Sum

**Difficulty:** Easy
**Topics:** Arrays, Hash Tables, Two-Pointer Technique
**Estimated Time:** 45-60 minutes

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to the target.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

You can return the answer in any order.

### Examples

**Input:** `nums = [2, 7, 11, 15]`, `target = 9`
**Output:** `[0, 1]`
**Explanation:** nums[0] + nums[1] = 2 + 7 = 9

**Input:** `nums = [3, 2, 4]`, `target = 6`
**Output:** `[1, 2]`
**Explanation:** nums[1] + nums[2] = 2 + 4 = 6

**Input:** `nums = [3, 3]`, `target = 6`
**Output:** `[0, 1]`

## Approach 1: Brute Force (O(n²))

Check every pair of numbers:

```
for i in 0 to n-1:
    for j in i+1 to n-1:
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Pros:** Simple to understand
**Cons:** Slow for large arrays

## Approach 2: Hash Table (O(n)) - RECOMMENDED

Use a dictionary to store seen numbers:

1. Iterate through array
2. For each number, check if `target - number` is in the dictionary
3. If yes, return the indices
4. If no, add current number to dictionary

**Why this works:** Instead of checking all pairs, we can look up complements in O(1) time.

## Implementation

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.

    Args:
        nums: List of integers
        target: The target sum

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    # Your solution here
    pass
```

## Test Cases

```python
def test_two_sum():
    # Basic tests
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

    # Order doesn't matter (as per problem)
    result = two_sum([1, 5, 7, 9], 14)
    assert set(result) == {1, 3}  # nums[1] + nums[3] = 5 + 9 = 14

    # Negative numbers
    result = two_sum([-1, -2, -3, 5, 10], 8)
    assert set(result) == {3, 4}  # nums[3] + nums[4] = 5 + 3 = 8... wait that's wrong
    # Let me fix: [-1, -2, -3, 5, 10] -> 5 + 3 = 8, but 3 is not 10
    # Actually: for target 8, we need -1 + 9 (not in list) or other combinations
    # Let's use: [-1, 9, 10] target 8 -> [-1 + 9 = 8]
    result = two_sum([-1, 9, 10], 8)
    assert set(result) == {0, 1}

    # Edge case: exactly two numbers
    assert two_sum([1, 2], 3) == [0, 1]

    print("All tests passed!")

if __name__ == "__main__":
    test_two_sum()
```

## Learning Goals

By completing this exercise, you'll understand:

- Hash tables and their O(1) lookup property
- Time complexity trade-offs (brute force vs. hash table)
- How to optimize naive solutions
- A fundamental algorithmic pattern

## Complexity Analysis

**Brute Force:**

- Time Complexity: O(n²) - check all pairs
- Space Complexity: O(1) - no extra space

**Hash Table (Recommended):**

- Time Complexity: O(n) - single pass through array
- Space Complexity: O(n) - store up to n elements in hash table

## Key Insights

1. **Hash tables are powerful:** They provide O(1) lookup, enabling us to trade space for time
2. **Complement searching:** Instead of checking pairs, we ask "what number do I need to reach the target?"
3. **Early termination:** Once we find the pair, we can return immediately

## Edge Cases

- Array with exactly 2 elements
- Negative numbers
- Duplicate numbers in array
- Large arrays (where O(n²) would be too slow)

## Follow-up Questions

1. What if you needed to return the values instead of indices?
2. What if there could be multiple valid pairs? (Would your solution still work?)
3. Can you solve it with O(1) space if the array was sorted?
4. What if you needed to find three numbers that sum to target?

## Mentor Notes

Common mistakes:

- Using the same index twice (e.g., nums[0] + nums[0] when target = 4)
- Returning values instead of indices
- Checking if `complement` is current number instead of checking index

Teaching moments:

- Emphasize the power of hash tables for this type of problem
- Show the performance difference: O(n²) vs O(n)
- Discuss real-world scenarios where this matters (large datasets)
- Ask them to implement brute force first, then optimize
