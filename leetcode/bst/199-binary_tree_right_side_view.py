# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            rightSide = None
            qlen = len(queue)

            for i in range(qlen):
                node = queue.pop(0)
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res