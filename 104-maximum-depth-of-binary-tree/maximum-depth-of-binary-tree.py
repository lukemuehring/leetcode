# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return max(1+ self.maxDepth(root.left), 1+ self.maxDepth(root.right))



       























        # Iterative DFS
        if root is None: 
            return 0

        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth, res)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        return res


        # Recursive DFS
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))        