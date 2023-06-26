class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        
        if root:
            queue.append(root)

        while queue:
            val = []
            for i in range(len(queue)):
                curr = queue.popleft()
                val.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(val)
        return res