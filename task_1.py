class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key)
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    cur.right = Node(key)
                    return
                cur = cur.right
            else:
                return


def find_min(root):
    if root is None:
        return None            # порожнє дерево
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.key


def find_min_rec(node):
    if node is None:
        return None
    if node.left is None:
        return node.key
    return find_min_rec(node.left)


if __name__ == "__main__":
    tree = BST()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    print(find_min(tree.root))
    print(find_min_rec(tree.root))
    print(find_min(None))