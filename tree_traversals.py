class Traversal(object):

    def __init__(self):
        self.holder = list()

    def visit(self, x):
        self.holder.append(x)

    def pre_order_traversal(self, root):
        if root:
            self.visit(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            self.visit(root.val)
            self.in_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            self.visit(root.val)