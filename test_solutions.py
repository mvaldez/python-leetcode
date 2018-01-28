import unittest
import solutions


class SolutionTest(unittest.TestCase):

    def test_find_words(self):
        result = solutions.find_words(["Hello", "Alaska", "Dad", "Peace"])
        self.assertEqual(["Alaska", "Dad"], result)

    def test_trimBST(self):
        root = solutions.TreeNode(3)
        solutions.insert_val(root, 0)
        solutions.insert_val(root, 4)
        solutions.insert_val(root, 2)
        solutions.insert_val(root, 1)

        self.assertEqual(solutions.breadth_first(solutions.trimBST(self, root, 1, 3)), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
