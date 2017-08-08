class TreeNode(object):

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Node(object):

    def __init__(self, v, n):
        self.val = v
        self.Next = n


def list_of_depths_helper(node, depth, store):
    if node is None:
        return
    else:
        if store.get(depth) is None:
            store[depth] = Node(node, None)
        else:
            curr = store[depth]
            while curr.Next:
                curr = curr.Next

            curr.Next = Node(node, None)

    list_of_depths_helper(node.left, depth+1, store)
    list_of_depths_helper(node.right, depth + 1, store)
    return


def list_of_depths(root):
    store = {}
    list_of_depths_helper(root, 0, store)
    return store


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def is_bst_helper_bu(self, root):  # Bottom up approach
        if root is None:
            return None, None, True
        else:
            min_left, max_left, is_bst_left = self.is_bst_helper(root.left)
            min_right, max_right, is_bst_right = self.is_bst_helper(root.right)
            if is_bst_left and is_bst_right:
                if max_left is None and min_right is None:
                    return root.val, root.val, True
                elif max_left is None:
                    return root.val, max_right, root.val < min_right
                elif min_right is None:
                    return min_left, root.val, max_left < root.val
                else:
                    return min_left, max_right, max_left < root.val < min_right

            return min_left, max_right, False

    def is_bst_helper_td(self, root, minv, maxv):  # Top down approach
        if root is None:
            return True
        else:
            if not minv < root.val < maxv:
                return False
            else:
                is_bst_left = self.is_bst_helper_td(root.left, minv, root.val)
                is_bst_right = self.is_bst_helper_td(root.right, root.val, maxv)
                return is_bst_left and is_bst_right

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_bst_helper_td(root, float('-inf'), float('inf'))


def find_inorder_successor(root, n):
    if n.right is not None:
        curr = n.right
        while curr.left:
            curr = curr.left
        return curr.val
    else:
        ret_val = None
        curr = root
        while curr.val != root.val:
            if curr.val < root.val:
                ret_val = root.val
                curr = curr.left
            else:
                curr = curr.right
        return ret_val




if __name__ == '__main__':
    root = TreeNode(4)
