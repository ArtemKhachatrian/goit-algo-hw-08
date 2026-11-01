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


def tree_sum(node):
    if node is None:
        return 0
    return node.key + tree_sum(node.left) + tree_sum(node.right)


def tree_sum_iter(root):
    if root is None:
        return 0
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.key
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total


if __name__ == "__main__":
    tree = BST()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    print(tree_sum(tree.root))
    print(tree_sum_iter(tree.root))
    print(tree_sum(None))