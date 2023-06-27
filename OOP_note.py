from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs (root, path, res):
        # exit condition
        if root.children == []:
            res.append("->".join(path)+"->"+str(root.val))
            return
        for child in root.children:
            if child: 
                #  dfs(child, path.append(str(root.val)), res) is incorrect. 
                # The list.append() method modifies the list in-place and returns None, 
                # so it shouldn't be used as an argument to the recursive call. 
                # Instead, you can use path + [str(root.val)] to create a new list with the updated path.
                dfs(child, path+[str(root.val)], res)
                print(path)
    res = []
    if root: dfs(root, [], res)
    return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
