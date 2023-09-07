class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    return root

def inOrder(root):
    if not root:
        return
    
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def bfs(root):
    res = []
    queue = []
    if root:
        queue.append(root)

    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.pop(0)
            res.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
    
    print(res)

def rightside(root):
    res = []
    queue = []

    if root:
        queue.append(root)

    while queue:
        rightSide = None
        lenQueue = len(queue)

        for i in range(lenQueue):
            node = queue.pop(0)
            if node:
                rightSide = node
                queue.append(node.left)
                queue.append(node.right)
        if rightSide:
            res.append(rightSide.val)

    return res


root = None
root = insert(root, 10)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 11)
root = insert(root, 15)

print(rightside(root))