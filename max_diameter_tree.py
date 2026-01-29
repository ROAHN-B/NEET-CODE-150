class Solution:
    def diameterOfBinaryTree(self, root ) -> int:
        self.ans=0
        def dfs(root):
            if root is None:
                return 0
            left_depth=dfs(root.left)
            right_depth=dfs(root.right)

            self.ans=max(self.ans,left_depth+right_depth)
            return max(left_depth,right_depth)+1
        dfs(root)
        return self.ans