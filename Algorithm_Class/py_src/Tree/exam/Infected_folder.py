class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# 트리 구조 구성
def build_tree(pairs):  
    node_map = {}   # 각 폴더 이름을 키로 하고, 대응되는 Node 객체를 값으로 하는 딕셔너리

    for parent, child in pairs:
        if parent not in node_map:
            node_map[parent] = Node(parent)
        if child not in node_map:
            node_map[child] = Node(child)
        # 부모의 children 리스트에 자식을 추가해서 트리 형태 구성
        node_map[parent].children.append(node_map[child])

    return node_map, node_map[pairs[0][0]]

# 트리의 루트 노드로부터 시작해서 노드 P와 q의 최소 공통 조상 찾기    
def rec(folder, p, q):
    if folder is None or folder == p or folder == q:
        return folder

    found = []
    for file in folder.children:
        res = rec(file, p, q)
        if res:
            found.append(res)

    if len(found) >= 2: # 자식 중에서 두 개 이상에서 p나 q를 찾음
        return folder   # 현재 노드가 공통 조상
    elif len(found) == 1:
        return found[0] # 찾은 자식 반환
    
def solution(folders, p, q):
    node_map, root = build_tree(folders)
    p = node_map[p]
    q = node_map[q]
    return rec(root, p, q).value


# 테스트
folders = [["root","media"],["media","images"],["media","videos"],["images","holiday"],["videos","concert"]]
print(solution(folders, "holiday", "concert"))   # 출력: media
folders = [["root","apps"],["apps","chrome"],["apps","vscode"]]
print(solution(folders, "chrome", "vscode"))  # 출력: apps
folders = [["root","usr"],["usr","bin"],["usr","local"],["bin","tools"]]
print(solution(folders, "bin", "tools")) # 출력: bin