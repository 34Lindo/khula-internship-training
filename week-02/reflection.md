# Week 2 Reflection

## Day 1 — Path Sum

### Topic

Binary Trees and Recursion

### Problem

Given the root of a binary tree and a target sum, determine whether there is a root-to-leaf path whose values add up to the target.

### What I learned

Day 1 of Week 2 introduced me to binary trees and recursion.

A binary tree is a data structure where each node can have at most two children:

- left child
- right child

A leaf is a node that has no children.

The Path Sum problem requires the path to end at a leaf, not just any node.

### TreeNode

I learned how to represent a tree node using a Python class:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

# Day 2 — Pascal's Triangle

## Topic

Arrays, nested lists, loops, and pattern recognition.

## Problem

Given an integer `num_rows`, generate the first `num_rows` rows of Pascal's Triangle.

Example:

```text
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
```
