# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#inorder: left -> root -> right
#postOrder: left -> right -> root

#useing postorder to find root, which is the last one
# post order tree rebuild problem
# last element of the postorder list is the root.
# We also know that wherever that value shows up in the inorder list, everything to the left is on the left side of the root node and everything on the right is on the rightside of the root node.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:


        in_left  = 0
        in_right = len(inorder) - 1


        def recursive_helper(in_left, in_right ):
            # when subtree is empty
            if in_left > in_right:
                return None

            # find the current root at the last of postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # find the index of root value
            index = inorder.index(root_val)


            # build right subtree
            root.right = recursive_helper(index+1, in_right)
            #build left subtree
            root.left = recursive_helper(in_left, index - 1)

            return root


        return recursive_helper(in_left, in_right)


