class Node:
    def __init__(self,data):
        self.data=data
        # self.parent=None
        self.right=None
        self.left=None

    def __repr__(self):
        return repr(self.data)
        # tree=[]
        # if self.data:
        #     tree.append(repr(self.data))
        # return ','.join(tree)

    def add_left(self,node):
        self.left=node
        # if node is not None:
        #     self.parent=self

    def add_right(self,node):
        self.right=node
        # if node is not None:
        #     self.parent=self




def create_tree():
    two=Node(2)
    seven=Node(7)
    nine=Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one=Node(1)
    six=Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five=Node(5)
    ten=Node(10)
    six.add_right(ten)
    six.add_left(five)
    eight=Node(8)
    nine.add_right(eight)
    three=Node(3)
    four=Node(4)
    eight.add_right(four)
    eight.add_left(three)
    return two


def pre_order(node):
    print(node,end=" ")
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node,end=" ")
    if node.right:
        in_order(node.right)

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node,end=" ")


root=create_tree()
print('PRE_ORDER TREE:--------------------->')
pre_order(root)

print('\nIN_ORDER TREE:--------------------->')
in_order(root)

print('\nPOST_ORDER TREE:--------------------->')
post_order(root)










