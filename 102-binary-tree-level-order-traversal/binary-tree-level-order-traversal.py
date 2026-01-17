# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            results = []
            if root is None:
                return results
            
            q = deque()
            q.append(root)
            while q:
                currLevel = []
                for i in range(len(q)):
                    currNode = q.popleft()
                    currLevel.append(currNode.val)
                    if currNode.left:
                        q.append(currNode.left)
                    if currNode.right:
                        q.append(currNode.right)
                results.append(currLevel)
            
            return results







        