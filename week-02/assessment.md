Week 2 Assessment

Day 1 — Path Sum

1. What is a binary tree?

A binary tree is a structure where each node can have up to two children:

A left child

A right child

2. What is a leaf?

A leaf is a node that does not have any children.

In the Path Sum exercise, the path must end at a leaf.

3. How did you solve the Path Sum problem?

I used recursion. For each node, I subtract its value from the target sum and then continue through the left and right children.

When I reach a leaf, I check whether the remaining sum is zero.

4. What did you learn from this exercise?

I learned how recursion can be used to move through a tree and how important it is to identify the correct stopping point or base case.

Day 2 — Pascal's Triangle

1. What is Pascal's Triangle?

Pascal's Triangle is a pattern of numbers where every row starts and ends with 1.

The numbers in the middle are calculated by adding the two numbers directly above them.

For example:

    1

1 1
1 2 1
1 3 3 1

2. What does a nested list mean?

A nested list is a list that contains other lists.

For example:

[
[1],
[1, 1],
[1, 2, 1]
]

3. How did you solve the problem?

I created each row one at a time.

The first and last values of a row are always 1. For the middle values, I used the values from the previous row.

4. What did you learn?

I learned how to work with lists inside other lists and how to use information from a previous row to create the next row.

Day 3 — Valid Palindrome

1. What is a palindrome?

A palindrome is a word or sentence that reads the same forwards and backwards after ignoring things such as spaces, punctuation and differences between uppercase and lowercase letters.

For example:

"A man, a plan, a canal: Panama"

is a palindrome.

2. How did you solve the problem?

I used two positions, one starting at the beginning of the string and one starting at the end.

I moved them towards each other while comparing the characters.

I also skipped characters that were not letters or numbers.

3. Why do we use two pointers?

The two pointers allow us to compare characters from both ends without creating another copy of the string.

4. What did you learn?

I learned how to work with individual characters in a string and how two pointers can make a problem easier to solve.

Day 4 — Linked List Cycle

1. What is a linked list?

A linked list is a collection of nodes where each node can point to another node.

2. What is a cycle in a linked list?

A cycle happens when a node points back to a node that has already been visited instead of eventually reaching the end of the list.

3. What is the Tortoise and Hare method?

It uses two pointers:

A slow pointer that moves one step at a time.

A fast pointer that moves two steps at a time.

If they meet, it means there is a cycle.

4. What did you learn?

I learned how linked lists work and how using two pointers moving at different speeds can help detect a cycle.

Day 5 — Binary Tree Preorder Traversal

1. What is tree traversal?

Tree traversal means visiting the nodes of a tree in a particular order.

2. What is preorder traversal?

Preorder traversal visits nodes in this order:

Root → Left → Right

3. What are two ways of solving the problem?

The exercise showed two approaches:

Recursion

Using a stack

4. What did you learn?

I learned that the same problem can sometimes be solved in different ways.

I found recursion easier to understand because it follows the structure of the tree.

Day 6 — Rising Temperature

1. What does the Rising Temperature exercise do?

The program looks at a list of temperatures and finds how many days we need to wait before getting a warmer temperature.

For example:

[73, 74, 75]

would give:

[1, 1, 0]

because:

74 is one day after 73.

75 is one day after 74.

There is no warmer temperature after 75.

2. How did you solve the problem?

I compared each temperature with the temperatures that came after it.

When I found a warmer temperature, I calculated how many positions away it was.

3. What did you learn?

I learned how to work with indexes in arrays and how nested loops can be used to compare values.

Day 7 — Reverse Bits

1. What does the Reverse Bits exercise do?

The program takes a 32-bit number and reverses the order of its bits.

2. How does the solution work?

The program takes the rightmost bit from the number and adds it to the result.

It then moves to the next bit until all 32 bits have been processed.

3. What does n & 1 do?

It allows us to check the rightmost bit of the number.

4. What does n >>= 1 do?

It shifts the bits of n one position to the right.

This allows the next bit to become the rightmost bit so it can be processed.

5. What did you learn?

I learned that numbers can be represented in binary and that Python allows us to work directly with individual bits.

Day 8 — Number of 1 Bits

1. What does the Number of 1 Bits exercise do?

The program counts how many 1s appear in the binary representation of a number.

For example:

11 = 1011

There are three 1s, so the answer is:

3

2. What is a binary representation?

Binary is a way of representing numbers using only two values:

0 and 1

3. What approaches were introduced?

The exercise showed different ways to count the 1 bits, including checking bits one at a time and using Python's built-in binary representation.

4. What did you learn?

I learned more about binary numbers and how computers can work with individual bits.

Day 9 — Next Permutation

1. What does the Next Permutation exercise do?

The program changes a list of numbers into the next possible ordering that is greater than the current ordering.

For example:

[1, 2, 3]

becomes:

[1, 3, 2]

2. What happens if there is no greater permutation?

If the numbers are already in descending order, there is no larger ordering.

The program then changes them into ascending order.

For example:

[3, 2, 1]

becomes:

[1, 2, 3]

3. What are the main steps?

The solution:

Finds the position where the ordering can be increased.

Finds a larger number to swap with it.

Swaps the numbers.

Rearranges the remaining numbers.

4. What did you learn?

I learned how to manipulate a list without creating a completely new list and how the order of numbers can be changed systematically.

Day 10 — Clone Graph

1. What does the Clone Graph exercise do?

The program creates a separate copy of a graph.

The copy should contain the same nodes and connections as the original graph.

2. Why do we need to keep track of nodes that have already been copied?

Graphs can contain connections that lead back to nodes we have already visited.

Keeping track of copied nodes prevents the program from repeatedly copying the same node.

3. What approaches can be used?

The exercise introduced:

Depth-First Search (DFS)

Breadth-First Search (BFS)

4. What did you learn?

I learned that graphs can contain connections in many directions and that we need to keep track of what we have already visited when working with them.

Task Manager CLI Project Assessment

1. What is the Task Manager CLI?

The Task Manager CLI is a program that allows users to manage tasks by typing commands into the terminal.

Instead of using a website with buttons, the user interacts with the program through the command line.

2. What does CLI mean?

CLI means Command Line Interface.

It is a way of interacting with a program by typing commands.

For example:

python main.py list

3. What does task.py do?

task.py contains the Task model.

It defines what information a task should have, such as:

ID

Description

Completed status

Priority

Creation date

4. What does storage.py do?

storage.py handles saving and loading tasks.

The tasks are stored in:

tasks.json

This means the tasks can still be available after the program is closed.

5. What does cli.py do?

cli.py contains the commands that the user can run from the terminal.

The commands I implemented are:

add
list
done
delete
edit
search
clear

6. What does main.py do?

main.py is the entry point of the program.

It starts the CLI application.

7. What is tasks.json used for?

tasks.json is used to permanently store the tasks.

It contains the task information in a format that Python can save and load.

8. What is the purpose of the tests folder?

The tests folder contains automated tests that check whether different parts of the application work correctly.

It contains:

tests/
├── test_task.py
├── test_storage.py
└── test_cli.py

9. What does test_task.py test?

It tests the Task model.

For example, it checks:

Creating tasks.

Different priorities.

Completed tasks.

Saving task information.

Loading task information.

Empty descriptions.

Invalid priorities.

10. What does test_storage.py test?

It tests whether tasks can be saved and loaded correctly.

It also tests deleting tasks, corrupted JSON and generating the next task ID.

11. What does test_cli.py test?

It tests the commands from the user's point of view.

It checks commands such as:

Adding tasks.

Listing tasks.

Completing tasks.

Deleting tasks.

Filtering tasks.

Editing tasks.

Searching tasks.

Clearing tasks.

12. How did you test the project?

I used pytest.

I ran:

pytest

The final result was:

38 passed

This showed that all 38 tests were passing.

13. Give an example of manually testing the application.

First, I can add a task:

python main.py add "Learn Python"

Then I can check that it appears:

python main.py list

I can mark it as complete:

python main.py done 1

Then I can list the tasks again and check that the task is marked as completed.

Finally, I can delete it:

python main.py delete 1

and check that it is no longer in the list.

14. How did you test errors?

I tested situations such as:

python main.py add "Test task" --priority urgent

The program correctly rejected the invalid priority.

I also tested an ID that does not exist:

python main.py done 999

The program responded:

Task 999 not found.

15. What was the biggest challenge during the project?

The biggest challenge was moving from building applications using HTML, CSS and JavaScript to building a Python application that works through the command line.

The terminal was initially unfamiliar to me, but I became more comfortable using it to run my program, test commands and find errors.

16. What did you learn from debugging?

I learned not to immediately change code when something goes wrong.

Instead, I learned to look at the error message, understand where the problem happened, make a change and run the tests again.

17. What did you learn about testing?

I learned that testing helps me find problems that I might not notice when manually running the program.

The tests also give me confidence that changes I make have not broken other parts of the application.

18. What was one of your biggest improvements during Week 2?

One of my biggest improvements was becoming more comfortable working in the terminal and using Python to build a complete application.

I also became more familiar with debugging, testing, Git and organising a project into different files where each file has a specific responsibility.
