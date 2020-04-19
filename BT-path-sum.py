# DFS inorder traversal to search for the target sum
# Solution 1: use while loop
class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # when root is null, return false
        if not root :
            return False



        stack = [(root, sum - root.val), ]
        while stack:
            curr_node, curr_sum = stack.pop()
            # if reached a leaf node and meet the target sum
            if  not curr_node.left and not curr_node.right and curr_sum == 0:
                return True


            if curr_node.left:
                stack.append((curr_node.left, curr_sum - curr_node.left.val))
            if curr_node.right:
                stack.append((curr_node.right, curr_sum - curr_node.right.val))
        return False

# Solution 2: recursive DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS inorder traversal to search for the target sum

class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # when root is null, return false
        if not root :
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

