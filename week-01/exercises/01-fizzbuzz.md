# Exercise 1: FizzBuzz

**Difficulty:** Easy
**Topics:** Conditionals, String Operations
**Estimated Time:** 30-45 minutes

## Problem Statement

Write a function that takes an integer `n` and prints numbers from 1 to n. However:

- For multiples of 3, print "Fizz" instead of the number
- For multiples of 5, print "Buzz" instead of the number
- For multiples of both 3 and 5, print "FizzBuzz" instead of the number

### Example

**Input:** `n = 15`

**Output:**

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## Approach

Before coding, think about:

1. How do you check if a number is a multiple of another number?
2. What's the order of conditions to check?
3. Should you check for 3 first, 5 first, or 15 first?

**Hint:** Consider checking for the most specific condition first (multiples of both).

## Implementation

```python
def fizzbuzz(n: int) -> list[str]:
    """
    Generate the fizzbuzz sequence from 1 to n.

    Args:
        n: The upper limit (inclusive)

    Returns:
        A list of strings representing the fizzbuzz sequence
    """
    # Your solution here
    pass
```

## Test Cases

```python
def test_fizzbuzz():
    # Basic test
    result = fizzbuzz(15)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
                "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert result == expected, "Basic test failed"

    # Small input
    result = fizzbuzz(3)
    expected = ["1", "2", "Fizz"]
    assert result == expected, "Small input test failed"

    # Edge case: n = 1
    result = fizzbuzz(1)
    expected = ["1"]
    assert result == expected, "Single element test failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_fizzbuzz()
```

## Learning Goals

By completing this exercise, you'll understand:

- How to use the modulo operator (`%`) to check divisibility
- How to construct conditional logic with multiple branches
- How to build a solution step-by-step
- How to write basic test cases

## Complexity Analysis

**Time Complexity:** O(n) - we iterate through each number from 1 to n
**Space Complexity:** O(n) - we store n strings in the output list

## Next Steps

Once you've solved this:

1. Can you optimize space by printing directly instead of returning a list?
2. What if you had to handle 7→"Zazz"? How would your code scale?
3. How would you handle this with a more elegant approach using a mapping?

## Mentor Notes

Common mistakes:

- Checking for 3 and 5 before checking for 15 (order matters!)
- Using `!=` instead of `%` for divisibility checks
- Returning numbers as integers instead of strings

Excellent follow-ups:

- Ask why we check 15 first (most specific case)
- Discuss how to extend this pattern for more divisors
- Talk about readability vs. cleverness in code
