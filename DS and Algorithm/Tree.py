from ds_2 import Queue
from BinaryTreePrinter import BinaryTreePrinter
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes =Queue()
            nodes.enqueue(self.root)



            while True:
                checking_node = nodes.dequeue()
                tree.append(nodes)

                if checking_node.left is None:
                    checking_node.left= TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)
    def __str__(self):
        tree_printer=BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


my_tree=BinaryTree()
# for c in ['a','b','c','d','e','f']:
#     my_tree.insert(c)

my_tree.insert('a')
my_tree.insert('b')
print(my_tree)
