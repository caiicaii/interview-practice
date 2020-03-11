# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.


def is_unival(root):
    return check_unival(root, root.value)


def check_unival(root, value):
    if root is None:
        return True
    if root.value == value:
        return check_unival(root.left, value) and check_unival(root.right, value)
    return False


def count_unival_subtrees(root):
    if root is None:
        return 0
    right = count_unival_subtrees(root.right)
    left = count_unival_subtrees(root.left)
    return 1 + right + left if is_unival(root) else right + left
