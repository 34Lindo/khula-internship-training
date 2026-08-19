Week 1 Assessment — Python Fundamentals & Problem Solving

Part A — Python Fundamentals

1. What is range(1, n + 1)?

Answer: range() excludes its stop value, so range(1, n + 1) processes 1 through n.

2. Does Python starting indexes at zero mean range always starts at zero?

Answer: No. List indexing starts at zero, but range() can start at any value.

3. What is %?

Answer: It returns the remainder after division. n % k == 0 is a common divisibility test.

4. Difference between /, //, and %?

Answer: / is regular division, // is floor division, and % is the remainder.

5. Why does indentation matter?

Answer: Python uses indentation to define blocks. Incorrect indentation can cause IndentationError or change program structure.

Part B — FizzBuzz

6. Explain your FizzBuzz solution.

Answer: Loop from 1 to n, check divisibility by 15 first, then 3, then 5, otherwise return the number as a string.

7. Why check 15 before 3 and 5?

Answer: 15 satisfies both conditions. The specific combined condition must be checked before the broader individual conditions.

8. FizzBuzz time complexity?

Answer: O(n) because each number is processed once.

9. FizzBuzz space complexity?

Answer: O(n) because the output list stores n values.

Part C — Palindrome

10. How do you extract the last digit?

Answer: number % 10.

11. How do you remove the last digit?

Answer: For positive integers, number // 10.

12. Why save original?

Answer: The loop changes number, so original preserves the starting value for comparison.

13. Why reject negative numbers?

Answer: The implemented solution defines negative integers as non-palindromes and returns False.

14. Complexity?

Answer: If the number has d digits, O(d) time and O(1) auxiliary space.

Part D — Two Sum

15. Key idea?

Answer: Calculate target - number, then check whether that complement has already been seen in a dictionary.

16. Why a dictionary?

Answer: Average O(1) lookup allows an O(n) average-time solution.

17. Why lookup before storing?

Answer: To prevent using the current element twice.

Part E — Merge Sorted Array

18. What do i, j, and k represent?

Answer: i is the last actual value in nums1, j is the last value in nums2, and k is the next position from the end of nums1.

19. Why merge backwards?

Answer: nums1 has free space at the back, so writing the largest values there avoids overwriting unprocessed values.

20. Complexity?

Answer: O(m+n) time and O(1) extra space.

Part F — Climbing Stairs

21. Explain the recurrence.

Answer: The final move comes from n-1 or n-2, so ways(n) = ways(n-1) + ways(n-2).

22. What is dynamic programming?

Answer: Solving overlapping subproblems and reusing their results instead of recalculating them.

23. Why O(1) space?

Answer: Only the previous two results are required, so we keep two variables.

Part G — Testing

24. What is pytest?

Answer: A Python testing framework used to automatically run tests and report whether expected behavior matches actual behavior.

25. What does -v mean?

Answer: Verbose test output.

26. What is AssertionError?

Answer: The test ran but actual output differed from expected output.

27. Can a test be wrong?

Answer: Yes. During Week 1 a test expected "fizz" while the implementation returned "Fizz". The expected value needed to match the required capitalization.

Part H — Debugging

28. ModuleNotFoundError?

Answer: Python could not locate the requested module in the current import context.

29. ImportError?

Answer: Python found the module but could not import the requested function/name.

30. IndentationError?

Answer: Python could not correctly parse the indentation structure.

31. My debugging process?

Answer: Read traceback → identify error → check file/line → check directory/environment → inspect code → make one focused fix → rerun targeted test → rerun full suite.

Part I — Environment

32. Where do I run cd?

Answer: PowerShell, not the Python >>> prompt.

33. Where do I run from solution import ...?

Answer: Inside Python, after starting Python from the correct solution directory.

34. Why can pytest be installed but still be unavailable?

Answer: Because different Python environments can have different installed packages. I used both Conda/base Python and a project .venv.

Part J — Git and PEP 8

35. What does git add do?

Answer: Stages changes.

36. What does git commit do?

Answer: Records staged changes in local Git history.

37. What does git push do?

Answer: Sends local commits to the remote repository.

38. Why use .gitignore?

Answer: To prevent generated files, caches and local environments from being version-controlled.

39. What is PEP 8?

Answer: Python's style guide for readable and consistent code.

Part K — Reflection

40. Biggest challenge?

Answer: Indentation, Python paths/environments, imports, and interpreting error messages.

41. Biggest breakthrough?

Answer: Learning to treat errors as information and use the traceback to guide the fix.

42. Problem-solving process?

Answer: Understand → Plan → Code → Test → Debug → Improve → Document → Commit → Push.

43. What do I need to improve?

Answer: Faster recognition of algorithmic patterns, especially recursion, trees, hash tables, two pointers and dynamic programming, plus more independent debugging.

Final Self-Assessment

-Python functions

-Type annotations

-Lists

-Dictionaries

-Loops

-Conditionals

-range()

-% and //

-FizzBuzz

-Integer reversal

-Palindrome

-Two Sum

--Two pointers

-Merge Sorted Array

-Dynamic programming

-Climbing Stairs

-Pytest

-Debugging

-Git

-PEP 8

-Time complexity

-Space complexity
