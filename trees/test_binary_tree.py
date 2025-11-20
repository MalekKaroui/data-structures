from binary_tree import BinaryTree

if __name__ == "__main__":
    tree = BinaryTree()
    for value in [10, 5, 15, 3, 7]:
        tree.insert(value)
    print("Inorder traversal:", end=" ")
    tree.inorder(tree.root)

