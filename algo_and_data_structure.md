# Data Structure and Algorithm Recap
By the end of the day, all data structures and algorithm questions can be break down to two base structure:
linked list and array. Tree, graph, Hash table, Queue, Stack, alll of them can be represented with the two basic structure.

### Tools & Materials :
- LeetCode Explore hase a Learn section, features Array and linkedlist
- Github Repo: fucking-algorithm



## Linked List


## Array

## Stack && Queue
In python, list can be used to implement stack and queue structure with build-in methods

```python


```

To implement a **queue**, use collections.deque which was designed to have fast appends and pops from both ends. For example:




## Graph

Following two are the most commonly used representations of a graph.
- Adjacency Matrix
- Adjacency List


## Hash Table


## Tree Traversal

There are two general strategies to traverse a tree:

#### Depth First Search (DFS)

In this strategy, we adopt the depth as the priority, so that one would start from a root and reach all the way down to certain leaf, and then back to root to reach another branch.

The DFS strategy can further be distinguished as preorder, inorder, and postorder depending on the relative order among the root node, left node and right node.

#### Breadth First Search (BFS)

We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher level would be visited before the ones with lower levels.

- Inorder (Left, Root, Right)
- Preorder (Root, Left, Right)
- Postorder (Left, Right, Root)
