def is_tree_balanced(root):
    return is_tree_balanced_helper(root)[1]


def is_tree_balanced_helper(root):
    if root is None:
        return 0, True
    else:
        left_height, is_left_balanced = is_tree_balanced_helper(root.left)
        right_height, is_right_balanced = is_tree_balanced_helper(root.right)
        if is_left_balanced and is_right_balanced and abs(left_height - right_height) <=1:
            return max([left_height, right_height]) + 1, True
        else:
            return -1, False
