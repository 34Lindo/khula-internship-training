# Week 1 Reflection — Python Fundamentals & Problem Solving

## Overview

Week 1 was my introduction to the Khula Junior Developer Internship problem-solving workflow. I learned not only to make code work, but to understand a problem, design an approach, implement it, test it, debug errors, evaluate complexity, and use Git professionally.

Problems Completed

1. FizzBuzz
2. Palindrome Number
3. Two Sum
4. Merge Sorted Array
5. Climbing Stairs

Day 1 — FizzBuzz

What I learned
I learned loops, `range()`, `if/elif/else`, modulo `%`, lists, `.append()`, `str()`, type annotations, testing, and Big-O.

```python
def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
```

Important lessons

- `range(1, n + 1)` processes 1 through n because the stop value is exclusive.
- List indexes start at 0; this is separate from the `range()` rule.
- `%` gives the remainder and is useful for divisibility.
- The combined FizzBuzz condition must come before Fizz and Buzz because conditions are evaluated from top to bottom.
- When conditions overlap, check the more specific condition first.
- Time complexity is `O(n)`.
- Space complexity is `O(n)` because the returned list stores n results.

Testing lesson
A test initially expected `"fizz"` while the function returned `"Fizz"`. I learned that tests compare exact values, including capitalization. The test was corrected and eventually all 7 FizzBuzz tests passed.

Day 2 — Palindrome Number

I learned how `% 10` extracts the last digit and `// 10` removes the last digit for positive integers.

```python
def reverse_number(number: int) -> int:
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number
```

For palindrome checking, I learned to preserve the original value before changing `number`.

```python
def is_palindrome(number: int) -> bool:
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number
```

Errors and lessons

- `IndentationError`: Python uses indentation as syntax, not decoration.
- `ModuleNotFoundError`: Python could not find `solution.py` from the current import context.
- I learned to exit the Python REPL, use PowerShell to `cd` into the correct solution folder, confirm the file exists, and then start Python.
- I learned that PowerShell commands such as `cd` and `Get-ChildItem` do not belong at the Python `>>>` prompt.

Day 3 — Two Sum

The key insight was to use a dictionary to remember values already seen.

```python
def two_sum(numbers: list[int], target: int) -> list[int]:
    seen = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []
```

The pattern is:

1. Calculate the complement.
2. Check whether it has already been seen.
3. If yes, return the indexes.
4. Otherwise store the current number.

This changes the average time from a brute-force `O(n²)` approach to `O(n)` using dictionary lookup, at the cost of `O(n)` extra space.

Day 4 — Merge Sorted Array

I learned the two-pointer technique and in-place modification.

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
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
```

I learned to merge from the back because `nums1` has free space at the back. This prevents overwriting values that still need to be processed.

Complexity:

- Time: `O(m + n)`
- Extra space: `O(1)`

I encountered an `ImportError` where Python found `solution.py` but could not import `merge`. I learned the difference between a missing module and a missing function/name inside an existing module.

Day 5 — Climbing Stairs

I learned dynamic programming and the recurrence:

`ways(n) = ways(n - 1) + ways(n - 2)`

The final step must come from either one stair below or two stairs below.

The optimized approach stores only the previous two answers, giving:

- Time: `O(n)`
- Space: `O(1)`

Testing and Pytest

I learned to run automated tests with:

```powershell
python -m pytest test_fizzbuzz.py -v
```

`-v` means verbose output.

I encountered `No module named pytest` because pytest was not installed in the Python environment being used. I installed it with `python -m pip install pytest`.

I also learned that a package installed in Conda/base Python may not exist in a project `.venv`. The Python environment matters.

Debugging Process

My debugging process became:

1. Read the complete traceback.
2. Identify the error type.
3. Find the file and line number.
4. Check my current directory and environment.
5. Inspect the relevant code.
6. Make one focused fix.
7. Run the smallest relevant test.
8. Run the full suite.

Python REPL vs PowerShell

PowerShell prompt:
`PS C:\...>`

Python prompt:
`>>>`

PowerShell:

```powershell
cd ...
Get-ChildItem
pwd
git status
git add .
git commit
git push
```

Python:

```python
from solution import fizzbuzz
print(fizzbuzz(15))
```

Mixing the two caused avoidable errors, and learning this distinction was important.

Indentation Lesson

Python uses indentation to define blocks:

```python
def example():
    value = 10
    return value
```

A missing or inconsistent indent can prevent an entire file from being imported or prevent pytest from collecting tests. I learned to treat indentation as part of Python syntax.

PEP 8 and Code Quality

I learned that PEP 8 is Python's style guide. Important practices include:

- 4-space indentation
- `snake_case`
- spaces around operators
- clear names
- readable formatting
- useful docstrings

Professional code should not only work; it should be readable, testable, and maintainable.

Git Lessons

I used my personal branch and learned:

```powershell
git status
git add .
git commit -m "message"
git push
```

I created `.gitignore` rules:

```text
__pycache__/
*.py[cod]
.venv/
.pytest_cache/
```

I learned that `.gitignore` prevents future files from being staged but does not automatically remove files already tracked.

What Went Well

- Completed the five Week 1 problems.
- Wrote automated tests.
- Reached a 7/7 passing FizzBuzz test suite.
- Learned to read tracebacks.
- Fixed path/import issues.
- Learned Python REPL vs PowerShell.
- Used Git commits and pushed my work.
- Became more comfortable with time and space complexity.
- Started thinking about edge cases.

What Was Difficult

- Python indentation
- `range()` and indexing
- `%` and `//`
- Condition ordering
- Imports and working directories
- Python environments and pytest
- Dictionaries in Two Sum
- Pointers in Merge Sorted Array
- Dynamic programming in Climbing Stairs

Biggest Lessons

1. Understand the problem before coding.
2. Work through examples manually.
3. Identify inputs, outputs, and edge cases.
4. Design the algorithm before implementation.
5. Test normal and edge cases.
6. Read error messages instead of guessing.
7. Check the environment before changing code.
8. Think about time and space complexity.
9. Write readable code.
10. Use Git to preserve and communicate progress.

Week 2 Goals

- Become faster at recognizing algorithmic patterns.
- Practice recursion and trees.
- Practice arrays and nested lists.
- Improve understanding of hash tables, two pointers, recursion and dynamic programming.
- Write tests more independently.
- Reduce avoidable path/import/indentation errors.
- Continue following PEP 8.
- Continue making meaningful Git commits.
- Build toward the Week 2 CLI project.

Final Reflection
Week 1 taught me that software development is not about getting the correct answer immediately. It is about developing a repeatable process:

**Understand → Plan → Code → Test → Debug → Improve → Document → Commit → Push**

The mistakes I made are part of my learning evidence. I now have a stronger process for investigating problems rather than guessing.
