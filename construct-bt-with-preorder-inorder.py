# Definition for a binary tree node.
class TreeNode:
       def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# preOrder : root -> left -> right
# inorder : left -> root -> right
# use preorder List to find the root, use inroder List for recursive_helper

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # start from first preorder element
        pre_idx = 0
        # build an hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}

        def recursive_helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = recursive_helper(in_left, index)
            # build right subtree
            root.right = recursive_helper(index + 1, in_right)
            return root


        return recursive_helper()


