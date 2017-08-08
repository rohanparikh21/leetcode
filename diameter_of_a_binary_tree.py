from binary_tree_tilt import TreeNode


class Solution(object):
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Keep track of the longest path encountered till now
        # Find the longest path passing through the root node
        if root is None:
            return 0
        diameter = 0
        left_height = self.height(root.left)
        diameter += (left_height if root.left else 0)
        right_height = self.height(root.right)
        diameter += (right_height if root.right else 0)
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    # right = TreeNode(3)
    root.left = left
    # root.right = right
    print Solution().diameterOfBinaryTree(root)