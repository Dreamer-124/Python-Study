class TreeNode:
    def __init__(self, key):
        """初始化树节点"""
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        """初始化一个空的二叉搜索树"""
        self.root = None

    def insert(self, key):
        """插入一个新节点"""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """递归插入帮助函数"""
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """查找一个节点"""
        return self._search(self.root, key)

    def _search(self, node, key):
        """递归查找帮助函数"""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """删除一个节点"""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """递归删除帮助函数"""
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        """找到最小值节点"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """中序遍历"""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """递归中序遍历帮助函数"""
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


# Example usage:
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder Traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

    node = bst.search(50)
    print("Search for 50:", "Found" if node else "Not Found")  # Output: Found

    node = bst.search(100)
    print("Search for 50:", "Found" if node else "Not Found")  # Output: Found

    bst.delete(20)
    print("Inorder Traversal after deleting 20:", bst.inorder_traversal())  # Output: [30, 40, 50, 60, 70, 80]

    bst.delete(30)
    print("Inorder Traversal after deleting 30:", bst.inorder_traversal())  # Output: [40, 50, 60, 70, 80]

    bst.delete(50)
    print("Inorder Traversal after deleting 50:", bst.inorder_traversal())  # Output: [40, 60, 70, 80]