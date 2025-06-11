# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            # print('wat')
            if root is None:
                return None

            if root is p or root is q:
                return root
            
            leftResult = dfs(root.left, p, q)
            rightResult = dfs(root.right, p, q)

            # print("root", root.val, "left",leftResult.val, "right",rightResult.val)
            if leftResult is not None and rightResult is not None:
                return root
            else:
                if leftResult:
                    return leftResult
                if rightResult:
                    return rightResult
                else:
                    return None
        # print('hello')
        return dfs(root,p,q)
            
