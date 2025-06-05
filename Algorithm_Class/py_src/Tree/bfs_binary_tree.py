from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_binary_tree(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)

    while queue:
        cur_node = queue.popleft()
        print(cur_node.value)   # 현재 노드의 값 출력

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# BFS 실행
print("bfs_bianry_tree")
bfs_binary_tree(root)


# 인접 리스트
def bfs(start, tree):
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        cur = queue.popleft()
        print(cur)  # 현재 방문한 노드 출력

        for next in tree.get(cur, []):
            if next not in visited:
                queue.append(next)
                visited.add(next)
    

# 인접 리스트로 트리 생성
tree = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

# BFS 실행
print("bfs_bianry_tree 인접리스트")
bfs(1, tree)
