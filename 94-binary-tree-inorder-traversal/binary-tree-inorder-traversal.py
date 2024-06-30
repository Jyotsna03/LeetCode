# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorderTraversal(root.left)    # Traverse the left subtree
            self.arr.append(root.val)           # Visit the root
            self.inorderTraversal(root.right)   # Traverse the right subtree
        return self.arr
        