class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_binary_tree(node):
    if node is None:
        return
    
    print(node.value)   # 현재 노드의 값 출력
    dfs_binary_tree(node.left)       # 왼쪽 자식 방문
    dfs_binary_tree(node.right)      # 오른쪽 자식 방문

# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# DFS 실행
print("dfs_bianry_tree (Preorder):")
dfs_binary_tree(root)


# 인접 리스트
def dfs(cur, visited):
    visited.add(cur)
    print(f"Visited: {cur}")    # 현재 방문한 노드 출력

    for next in tree[cur]:
        if next not in visited:
            dfs(next, visited)

# 인접 리스트로 트리 생성
tree = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

# DFS 실행
print("dfs_bianry_tree 인접리스트:")
visited = set()
dfs(1, visited)