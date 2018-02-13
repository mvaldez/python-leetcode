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


def callPoints(self, ops):
        """
        Given a list of strings, each string can be one of the 4 following types:

        Integer (one round's score): Directly represents the number of points you get in this round.

            "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
            "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
            "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
        :param self:
        :param ops:
        :return:
        """
        tokens = ["+", "D", "C"]
        sum = 0
        valid_input = []

        for op in ops:
            if op in tokens:
                if op == "+":
                    # sum last 2 valid inputs
                    p = sumTwo(valid_input)
                    sum += p
                    valid_input.append(p)
                if op == "D":
                    # double the last valid input
                    if valid_input:
                        d = valid_input.pop()
                        sum += d + d
                        valid_input.append(d)
                        valid_input.append(d + d)
                if op == "C":
                    # substract last valid input
                    if valid_input:
                        d = valid_input.pop()
                        sum -= d
            else:
                sum += int(op)
                valid_input.append(int(op))

        return sum


def sumTwo(stack):
    if not stack:
        return 0
    if len(stack) > 1:
        s1 = stack.pop()
        s2 = stack.pop()
        stack.append(s2)
        stack.append(s1)
        return s1 + s2
    if len(stack) == 1:
        return stack[0]


def findDisappearedNumbers(self, nums):
    val = len(nums)
    s = {n for n in range(1, val+1)}
    for n in nums:
        try:
            s.remove(n)
        except KeyError:
            pass
    return list(s)
