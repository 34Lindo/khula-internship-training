# Exercise 5: Climbing Stairs

**Difficulty:** Easy
**Topics:** Dynamic Programming, Recursion, Memoization
**Estimated Time:** 45-60 minutes

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can climb either 1 or 2 steps. In how many distinct ways can you climb to the top?

### Examples

**Input:** `n = 2`
**Output:** `2`
**Explanation:**

- 1 step + 1 step
- 2 steps

**Input:** `n = 3`
**Output:** `3`
**Explanation:**

- 1 step + 1 step + 1 step
- 1 step + 2 steps
- 2 steps + 1 step

**Input:** `n = 4`
**Output:** `5`
**Explanation:**

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2

## Key Insight

Think about it recursively: **To reach step n, you could have come from step (n-1) or step (n-2).**

So: `ways(n) = ways(n-1) + ways(n-2)`

This is the **Fibonacci sequence**!

## Approach 1: Naive Recursion (Slow - Don't use!)

```python
def climbStairs(n):
    if n <= 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)
```

**Problem:** Recalculates same values many times. Very slow!

## Approach 2: Memoization (Better)

Use a dictionary to store already-calculated values:

```python
def climbStairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
    return memo[n]
```

## Approach 3: Dynamic Programming (Best)

Build the solution bottom-up:

```
dp[0] = 1  (one way to reach step 0: don't climb)
dp[1] = 1  (one way to reach step 1: take 1 step)
dp[2] = 2  (two ways to reach step 2: 1+1, or 2)
...
dp[n] = dp[n-1] + dp[n-2]
```

## Implementation

```python
def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs.

    You can climb 1 or 2 steps at a time.

    Args:
        n: Number of stairs

    Returns:
        Number of distinct ways to climb to the top
    """
    # Your solution here
    pass
```

## Test Cases

```python
def test_climb_stairs():
    # Basic tests
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8

    # Larger values (to test efficiency)
    assert climb_stairs(10) == 89
    assert climb_stairs(20) == 10946

    print("All tests passed!")

if __name__ == "__main__":
    test_climb_stairs()
```

## Learning Goals

By completing this exercise, you'll understand:

- **Dynamic Programming:** Solving problems by breaking them into subproblems
- **Memoization:** Caching results to avoid redundant calculations
- **Optimization:** How to recognize and fix inefficient solutions
- **Fibonacci patterns:** Recognizing when problems have recursive structure

## Complexity Analysis

**Approach 1 (Naive Recursion):**

- Time Complexity: O(2^n) - VERY SLOW, exponential!
- Space Complexity: O(n) - call stack depth

**Approach 2 (Memoization):**

- Time Complexity: O(n) - calculate each value once
- Space Complexity: O(n) - memo dictionary + call stack

**Approach 3 (DP Bottom-Up) - Recommended:**

- Time Complexity: O(n) - single loop
- Space Complexity: O(n) - dp array

**Approach 4 (Space-Optimized DP):**

- Time Complexity: O(n)
- Space Complexity: O(1) - only store last two values!

## Space Optimization Hint

Notice that `dp[n]` only depends on `dp[n-1]` and `dp[n-2]`.

You don't need to store the entire dp array! Just keep track of the last two values:

```python
prev2, prev1 = 1, 1
for i in range(2, n+1):
    current = prev1 + prev2
    prev2, prev1 = prev1, current
return prev1
```

This reduces space complexity to O(1)!

## Visualization

```
n=4:

Step 0: 1 way
Step 1: 1 way
Step 2: 2 ways (from 0→1→2 or 0→2)
Step 3: 3 ways (from 2→3 with 2 ways, from 1→3 with 1 way)
Step 4: 5 ways (from 3→4 with 3 ways, from 2→4 with 2 ways)

      ways[0]=1
      ways[1]=1
      ways[2]=2
      ways[3]=3
      ways[4]=5
```

## Edge Cases

- n = 0 (no stairs)
- n = 1 (only one way)
- n = 2 (two ways)
- Large n (test efficiency)

## Follow-up Questions

1. Can you implement all three approaches? Which is clearest?
2. What if you could climb 1, 2, or 3 steps? How would this change?
3. Why is the recursive approach so slow? Can you trace through an example?
4. Can you reduce space complexity further (yes, see hint above!)

## Important Concepts

### Dynamic Programming

DP is powerful when problems have:

1. **Optimal substructure:** Solution is built from solutions to subproblems
2. **Overlapping subproblems:** Same subproblems appear multiple times

Climbing stairs has both!

### Memoization

Memoization is "remember the answer so you don't calculate it again."

It transforms exponential time to linear time by caching results.

## Mentor Notes

Common mistakes:

- Trying recursive without memoization (will timeout on large n)
- Off-by-one errors in DP indexing
- Not recognizing the Fibonacci pattern

Teaching moments:

- Show them what happens with naive recursion on n=40 (very slow!)
- Discuss why memoization helps (avoiding recalculation)
- Introduce the concept of dynamic programming formally
- Ask: "Can you do this iteratively instead of recursively?"
- Challenge: "Can you do it with O(1) space?"

Stretch goals:

- Implement all three approaches
- Optimize to O(1) space
- Extend to "can climb 1, 2, or 3 steps"
- Solve using matrix exponentiation (advanced)
