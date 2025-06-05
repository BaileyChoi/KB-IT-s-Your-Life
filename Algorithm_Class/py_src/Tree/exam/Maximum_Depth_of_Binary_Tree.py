from collections import deque

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root:TreeNode):
    if root is None:    # 기저 조건(base case)
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# 테스트
tree = build_tree([3, 9, 20, None, None, 15, 7])
print(maxDepth(tree))  # 출력: 3

tree2 = build_tree([1, None, 2])
print(maxDepth(tree2))  # 출력: 2