class TreeNode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.left=None
        self.right=None

    def __repr__(self):
        return repr(self.data)


    def add_left(self,node):
        self.left=node
        if node is not None:
            self.parent=self
            print(self.parent)


    def add_right(self,node):
        self.right=node
        if node is not None:
            self.parent=self
            print(self.parent)


def bst_insert(root,node):
    last_node=None
    current_node=node

    while current_node is not None:

        last_node=current_node
        # print('1------->', node.data)
        # print('2------->',current_node.data)
        if node.data< current_node.data:
            current_node=current_node.left
        else:
            current_node=current_node.right

    if last_node is None:
        root=node

    # print('3-------->',node.data,last_node.data)
    if node.data<last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root

def create_bst():
    root=TreeNode(10)

    for item in [5,17,3,7,12,19,1,4]:
        node=TreeNode(item)
        root=bst_insert(root,node)
    return root

# root=create_bst()
# print(root)
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)
root=create_bst()
print(in_order(root))