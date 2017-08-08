class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def subTreeSum(self, root):
        if root is None:
            return 0
        else:
            return self.subTreeSum(root.left) + self.subTreeSum(root.right) + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.findTilt(root.left) + self.findTilt(root.right) + abs(
            self.subTreeSum(root.left) - self.subTreeSum(root.right))

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print Solution().findTilt(root)