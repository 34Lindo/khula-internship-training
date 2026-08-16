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
