# Solutions to leetcode problems
# Author: markvaldez@gmail.com


def find_words(words):
    """
    Given a List of words, return the words that
    can be typed using letters of alphabet on
    only one row's of American keyboard
    :type words: List[str]
    :rtype: List[str]
    """
    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    results = []
    for word in words:
        if check_row(word, row1):
            results.append(word)
        if check_row(word, row2):
            results.append(word)
        if check_row(word, row3):
            results.append(word)
    return results


def check_row(word, row):
    for c in word:
        if c.lower() not in row:
            return False
    return True


class TreeNode(object):
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def to_list(node):
    return to_collection([], node)


def to_collection(mlist, node):
    if node:
        to_collection(mlist, node.left)
        mlist.append(node.val)
        to_collection(mlist, node.right)
    return mlist


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)


def inorder_collect(result, node, l, h):
    if node:
        inorder_collect(result, node.left, l, h)
        if l <= node.val <= h:
            result.append(node.val)
        inorder_collect(result, node.right, l, h)
    return result


def breadth_first(node):
    result = []
    if node is None:
        return result

    queue = [node]

    while len(queue) > 0:
        result.append(queue[0].val)
        n = queue.pop(0)

        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)

    return result


def insert_val(root, x):
    if x > root.val:
        if root.right is None:
            root.right = TreeNode(x)
        else:
            insert_val(root.right, x)
    else:
        if root.left is None:
            root.left = TreeNode(x)
        else:
            insert_val(root.left, x)


def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    result = [n for n in breadth_first(root) if L <= n <= R]
    root = TreeNode(result[0])
    for r in result[1::]:
        insert_val(root, r)
    return root


def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are
        jewels, and S representing the stones you have.  Each character
        in S is a type of stone you have.  You want to know how many of
        the stones you have are also jewels.
        :type J: str the jewel
        :type S: str the stone
        :rtype: int jewel count
        """
        letter_counts = {letter: S.count(letter) for letter in S}
        stone_count = 0
        for c in J:
            if c in letter_counts:
                stone_count += letter_counts.get(c)
        return stone_count
