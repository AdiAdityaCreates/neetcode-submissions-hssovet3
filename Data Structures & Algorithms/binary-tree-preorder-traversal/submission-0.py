# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(root,res):
    if root is None:
        return []
    res.append(root.val)
    preorder(root.left,res)
    preorder(root.right,res)
    return res
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return preorder(root,res)
        