import sys
class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        raddr = laddr = None
        if self.left:
            laddr = "BinaryNode at " + hex(id(self.left))
        if self.right:
            raddr = "BinaryNode at " + hex(id(self.right))
        return "<BinaryNode at {}, data: {}, left: {}, right: {}>".format(hex(id(self)), self.data, laddr, raddr)

def print_tree(root):
    if root.left != None:
        print_tree(root.left)
    print(root.data)
    if root.right != None:
        print_tree(root.right)

a_node = BinaryNode('A')
# print(sys.getsizeof(a_node))    # size in bytes
# print(id(a_node))   # id is an integer
# print(hex(id(a_node)))   # memory addresses are usually in hex
b_node=BinaryNode('B')
c_node=BinaryNode('C')
a_node.left=b_node
a_node.right=c_node

print_tree(a_node)
print(a_node.left.data,a_node.data,a_node.right.data)
