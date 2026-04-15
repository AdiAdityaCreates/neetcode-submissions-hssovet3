class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  
        
        def height(node):
            if node is None:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            
            self.res = max(self.res, left + right)
            
            
            return 1 + max(left, right)
        
        height(root)
        return self.res