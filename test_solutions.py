# import unittest
import solutions
import pytest


class TestSolutions(object):

    def test_find_words(self):
        result = solutions.find_words(["Hello", "Alaska", "Dad", "Peace"])
        assert ["Alaska", "Dad"] == result

    def test_trimBST(self):
        root = solutions.TreeNode(3)
        solutions.insert_val(root, 0)
        solutions.insert_val(root, 4)
        solutions.insert_val(root, 2)
        solutions.insert_val(root, 1)

        assert solutions.breadth_first(solutions.trimBST(self, root, 1, 3)) == [3, 2, 1]

    def test_jewels(self):
        J1 = "aA"
        S1 = "aAAbbbb"

        J2 = "z"
        S2 = "ZZ"

        assert solutions.numJewelsInStones(self, J1, S1) == 3
        assert solutions.numJewelsInStones(self, J2, S2) == 0

    def test_callPoints(self):
        input_1 = ["5","2","C","D","+"]
        input_2 = ["5","-2","4","C","D","9","+","+"]
        expected_1 = 30
        expected_2 = 27

        assert solutions.callPoints(self, input_1) == expected_1
        assert solutions.callPoints(self, input_2) == expected_2

    def test_findDisappearedNumbers(self):
        input = [4,3,2,7,8,2,3,1]
        output = [5,6]

        assert output == solutions.findDisappearedNumbers(self, input)

    def test_rotate_string(self):
        input = 'abcde'
        output = 'cdeab'

        assert solutions.rotateString(self, input, output)

