# Week 2 Reflection

Week 2 was a very different experience for me because I moved from solving simple programming exercises to working with more complex data structures and then building a complete command-line application.

At the beginning of the week, I was still trying to understand how some of the problems worked. By the end of the week, I had become more comfortable reading problems, breaking them down, writing solutions, testing my code, and fixing errors.

---

## Day 1 — Path Sum

### Topic

Binary Trees and Recursion

### What the exercise does

The Path Sum exercise asks us to look at a binary tree and determine whether there is a path from the top of the tree to the end of a branch where the numbers add up to a given target.

For example, if the target is 22, the program checks whether there is a path whose values add up to 22.

### What I learned

I learned what a binary tree is and how each part of the tree can have a left and right side.

I also learned about recursion. Instead of trying to check everything at once, the program can check one part of the tree and then continue checking the smaller parts.

The biggest thing I learned was the importance of a **base case**. The program needs to know when to stop checking.

---

## Day 2 — Pascal's Triangle

### Topic

Arrays, Lists and Patterns

### What the exercise does

Pascal's Triangle is a triangle of numbers where the first and last number of every row are 1. The numbers in the middle are created by adding the two numbers directly above them.

For example:

```text
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
Day 3 — Valid Palindrome

Topic

Strings and Two Pointers

What the exercise does

The program checks whether a sentence or word reads the same forwards and backwards.

It ignores spaces, punctuation, and differences between uppercase and lowercase letters.

For example:

"A man, a plan, a canal: Panama"

is considered a palindrome.

What I learned

I learned how to work with individual characters in a string.

I also learned the two-pointer idea, where one pointer starts from the beginning and another starts from the end. They move towards each other while comparing the characters.

This showed me that I don't always need to create another copy of the data to solve a problem.

Day 4 — Linked List Cycle

Topic

Linked Lists

What the exercise does

The program checks whether a linked list contains a cycle.

A cycle happens when a node eventually points back to a node that was already visited instead of reaching the end of the list.

What I learned

I learned about linked lists and how nodes can point to other nodes.

I also learned about Floyd's Cycle Detection Algorithm, also known as the Tortoise and Hare method.

The idea is to have:

A slow pointer that moves one step at a time.

A fast pointer that moves two steps at a time.

If they eventually meet, there is a cycle.

This exercise helped me understand how using two different speeds can help solve a problem without needing a lot of extra memory.

Day 5 — Binary Tree Preorder Traversal

Topic

Trees and Traversal

What the exercise does

The program visits every node in a binary tree in a specific order.

For preorder traversal, the order is:

Root → Left → Right

For example:

    1
     \
      2
     /
    3

would produce:

[1, 2, 3]

What I learned

I learned that there are different ways of visiting the nodes in a tree.

I also saw two ways of solving the problem:

Using recursion.

Using a stack.

The recursive approach was easier for me to understand because it follows the structure of the tree naturally.

Task Manager CLI Project

After working through the exercises, I worked on the Task Manager CLI project.

This was probably the biggest learning experience of Week 2 because I had to combine several things I had learned into one working application.

What the project does

The Task Manager is a simple program that allows a user to manage tasks from the command line.

Instead of using a website with buttons and forms, I interact with the application by typing commands into the terminal.

For example:

python main.py add "Learn Python" --priority high

The application then creates the task and gives it an ID.

I can also list tasks:

python main.py list

Mark a task as complete:

python main.py done 1

Delete a task:

python main.py delete 1

I also added extra features such as:

python main.py list --status pending
python main.py list --priority high
python main.py edit 1 "Updated task"
python main.py search "Python"
python main.py clear --confirm

Project Structure

main.py

This is the entry point of the application.

It starts the command-line program and connects it to the commands in cli.py.

task.py

This contains the Task model.

It represents what a task looks like.

A task has information such as:

ID

Description

Completed status

Priority

Date it was created

It also contains the functions needed to convert a task into information that can be saved and to recreate a task from saved information.

storage.py

This handles saving and loading tasks.

The application stores the tasks in a file called:

tasks.json

The storage code makes sure that tasks don't disappear when the program is closed.

It can:

Load tasks

Save tasks

Add tasks

Delete tasks

Find a task by its ID

Return all tasks

cli.py

CLI means Command Line Interface.

This is the part of the project that handles the commands I type into the terminal.

For example:

python main.py add "Learn Python"

The CLI receives the command, understands what I want to do, and then communicates with the rest of the program.

The commands I implemented include:

add

list

done

delete

edit

search

clear

tests/

The tests folder contains the tests for the application.

It is divided into:

tests/
├── test_task.py
├── test_storage.py
└── test_cli.py

test_task.py

These tests check that the Task model works correctly.

For example, they check that:

A task can be created.

Priorities work.

Completed tasks work.

Task information can be converted into saved data.

Saved task information can be converted back into a task.

Empty descriptions are rejected.

Invalid priorities are rejected.

test_storage.py

These tests check the saving and loading of tasks.

They test things such as:

Starting with no file.

Saving a task.

Loading a task.

Saving completed tasks.

Saving multiple tasks.

Deleting tasks.

Handling corrupted JSON.

Generating the next task ID.

test_cli.py

These tests check whether the commands work correctly from the user's point of view.

They test:

Adding tasks.

Adding tasks with different priorities.

Listing tasks.

Marking tasks as complete.

Deleting tasks.

Filtering tasks.

Editing tasks.

Searching for tasks.

Clearing tasks.

Handling invalid task IDs.

How I Tested the Project

I used pytest to test the application.

I ran:

pytest

The final test result was:

38 passed

This was important to me because it showed that the different parts of my application were working as expected.

I also manually tested the commands through the terminal.

For example, I could add a task:

python main.py add "Learn Python"

Then check that it appears:

python main.py list

I could mark it as complete:

python main.py done 1

Then list the tasks again and see:

1 | [x] | Learn Python | Normal

I could also delete a task:

python main.py delete 1

and check that it was no longer in the list.

I tested invalid situations as well, such as trying to use an invalid priority or trying to complete a task ID that does not exist.

Challenges I Faced

One of my biggest challenges was that I was more familiar with building things using HTML, CSS, and JavaScript.

I had previously thought about applications such as a to-do list where a user interacts with a webpage.

The Task Manager project was different because I was using Python and a command-line interface instead.

At first, working in the terminal felt unfamiliar, but throughout the project I became more comfortable running commands, checking results, and using the terminal to interact with my program.

Another challenge was debugging.

There were times when my tests failed or when the program did not behave as I expected. Instead of just changing the code randomly, I learned to look at the error message, find where the problem was happening, and then fix it.

I also learned how important testing is because the tests helped me find problems that I might not have noticed by simply running the program once.
```
