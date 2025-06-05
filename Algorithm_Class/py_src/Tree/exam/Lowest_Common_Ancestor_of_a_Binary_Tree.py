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

def find_node_by_val(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node_by_val(root.left, val)
    if left:
        return left
    return find_node_by_val(root.right, val)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) :
    return rec(root, p, q)

def rec(root, p, q):
    # 현재 노드 검사
    if root is None or root == p or root == q:
        return root
    
    # 왼쪽/오른쪽 서브트리 탐색
    left = rec(root.left, p, q)
    right = rec(root.right, p, q)

    # 공통 조상 판단
    if left and right:  # p와 q가 양쪽에 하나씩 있는 경우
        return root 

    return left if left else right  # 둘 중 하나만 존재하는 경우

# 테스트
tree = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p = find_node_by_val(tree, 5)
q = find_node_by_val(tree, 1)
print(lowestCommonAncestor(tree, p, q).val)  # 출력: 3

# 테스트 2
tree = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p = find_node_by_val(tree, 5)
q = find_node_by_val(tree, 4)
print(lowestCommonAncestor(tree, p, q).val)  # 출력: 5

# 테스트 3
tree = build_tree([1,2])
p = find_node_by_val(tree, 1)
q = find_node_by_val(tree, 2)
print(lowestCommonAncestor(tree, p, q).val)  # 출력: 1