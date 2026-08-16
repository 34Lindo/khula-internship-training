# Day 2 Reflection — Palindrome Number

## What I Learned

Today I learned how to work with individual digits of an integer using:

- `% 10` to extract the last digit
- `// 10` to remove the last digit
- Multiplication by 10 to build a reversed number
- Boolean comparisons to determine whether a number is a palindrome

I also learned how to separate responsibilities between functions. The
`reverse_number()` function is responsible for reversing a number, while
`is_palindrome()` determines whether the original number is equal to its
reverse.

## Problem-Solving Approach

1. Check whether the number is negative.
2. Save the original number.
3. Reverse the number.
4. Compare the original number with the reversed number.
5. Return `True` if they are equal, otherwise `False`.

## Errors I Encountered

### 1. IndentationError

I initially placed code at the wrong indentation level.

### Lesson

Python uses indentation to define code blocks. I learned that indentation
is not just formatting; it affects program behavior.

### 2. Return Inside the While Loop

I initially placed `return reversed_number` inside the `while` loop. This
caused the function to return after processing only the first digit.

For example:

`123` incorrectly returned `3` instead of `321`.

### Lesson

A `return` statement immediately exits the function. It therefore needed to
be placed after the loop so every digit could be processed.

### 3. Python and PowerShell Confusion

I accidentally entered PowerShell commands such as `cd`, `pwd`, and
`python -m pytest` inside the Python interpreter.

### Lesson

I learned to distinguish between:

- `>>>` — Python interpreter
- `PS ...>` — PowerShell terminal

### 4. ModuleNotFoundError

Python initially could not find `solution.py` because I was running Python
from the wrong directory.

### Lesson

The current working directory matters when importing local Python modules.

### 5. Pytest Environment

Pytest was installed in my base environment but was not available inside
the Khula `.venv`.

### Lesson

Python packages are installed into specific environments. I need to make
sure I install dependencies into the environment my project is actually
using.

## Testing

I tested:

- `121` → `True`
- `123` → `False`
- `1221` → `True`
- `10` → `False`
- `-121` → `False`
- `0` → `True`
- `7` → `True`

## Complexity

For a number with `d` digits:

- Time complexity: `O(d)`
- Space complexity: `O(1)`

## Key Lesson

Debugging is not just fixing syntax errors. I learned to identify whether
a problem comes from my code, indentation, environment, file location,
dependencies, or tests.

## Day 3 Reflection — Two Sum

### What I Learned

Today I learned how Python dictionaries can be used as hash tables to
perform fast lookups. I learned that a dictionary stores key-value pairs
and that lookup is approximately O(1).

I learned the Two Sum pattern:

1. Iterate through the list once.
2. Calculate the complement using `target - number`.
3. Check whether the complement already exists in the dictionary.
4. If it exists, return the stored index and current index.
5. Otherwise, store the current number and its index.

### Key Concept

The dictionary approach improves the typical brute-force O(n²) solution
to O(n) time at the cost of O(n) additional space.

### Important Lesson

The lookup must happen before storing the current number. This prevents
using the same array element twice.

### New Python Concept

I used `enumerate()` to obtain both the index and value while iterating
through a list.

### Testing

I tested:

- Normal Two Sum example
- Pair in the middle
- Duplicate values
- Negative numbers
- Pair at the end
- No-solution case

### Problem-Solving Lesson

Instead of repeatedly searching the entire list, I learned to ask:

"What information can I remember so that I don't have to search again?"

This led to the hash-table solution.

## Day 4 Reflection — Merge Sorted Array

### What I Learned

Today I learned the two-pointer technique using the Merge Sorted Array
problem.

The important idea was to work backwards from the end of the arrays.
This allows the algorithm to use the empty space already available in
`nums1` without overwriting values that still need to be processed.

### Three Pointers

I used three indexes:

- `i = m - 1` — last actual element in `nums1`
- `j = n - 1` — last element in `nums2`
- `k = m + n - 1` — final position in `nums1`

At every step I compare `nums1[i]` and `nums2[j]` and place the larger
value at `nums1[k]`.

### Important Insight

Working backwards is important because `nums1` already contains empty
positions at the end. Starting from the beginning could overwrite values
that have not yet been processed.

### Errors and Debugging

I initially encountered an import error:

`ImportError: cannot import name 'merge' from 'solution'`

The path was correct and Python found `solution.py`, so the problem was
inside the file rather than the directory.

This reminded me to distinguish between:

- `ModuleNotFoundError` — Python cannot find the module.
- `ImportError` — Python found the module but cannot find the requested
  function or object inside it.

### Testing

I tested:

- Normal merge
- Empty second array
- Empty first array
- Values in `nums2` smaller than `nums1`
- Duplicate values
- Single-element arrays

### Complexity

Time complexity: `O(m + n)`

Space complexity: `O(1)`

### Key Lesson

The two-pointer technique can solve array problems efficiently by using
indexes to avoid unnecessary additional data structures.
