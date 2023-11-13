from collections import deque
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, des in edges:
    if src not in adjList:
        adjList[src] = []
    if des not in adjList:
        adjList[des] = []
    adjList[src].append(des)

# how many path
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
    return count 


# shortest path
def bfs(node, target, adjList):
    length = 0
    queue = deque()
    visit = set()
    queue.append(node)
    visit.add(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for n in adjList[curr]:
                if n not in visit:
                    visit.add(n)
                    queue.append(n)
        length += 1
    return length

print(bfs("A", "E", adjList))