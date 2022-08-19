import unittest
from logics import *

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1+1, 2)

    def test_2(self):
        self.assertEqual(get_number_from_index(2, 3), 12)

    def test_3(self):
        self.assertEqual(get_number_from_index(3, 0), 13)

    def test_4(self):
        a = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16]
        mas = [[0, 0, 0, 0],
               [0, 0, 2, 0],
               [0, 0, 0, 0],
               [4, 0, 0, 0]]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        a = []
        mas = [[1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4]]
        self.assertEqual(get_empty_list(mas), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(12), (2, 3))

    def test_7(self):
        self.assertEqual(get_index_from_number(13), (3, 0))

    def test_8(self):
        mas = [[0, 0, 0, 0],
               [0, 0, 2, 0],
               [0, 0, 0, 0],
               [4, 0, 0, 0]]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_9(self):
        mas = [[1, 3, 5, 7],
               [1, 3, 5, 7],
               [1, 3, 5, 7],
               [1, 3, 5, 7]]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_10(self):
        mas = [[0, 0, 0, 0],
               [0, 2, 2, 0],
               [0, 0, 0, 0],
               [4, 4, 0, 0]]

        res = [[0, 0, 0, 0],
               [4, 0, 0, 0],
               [0, 0, 0, 0],
               [8, 0, 0, 0]]
        self.assertEqual(move_left(mas), (res, 12))

    def test_11(self):
        mas = [[0, 0, 0, 0],
               [0, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        res = [[0, 0, 0, 0],
               [4, 0, 0, 0],
               [8, 0, 0, 0],
               [4, 0, 0, 0]]
        self.assertEqual(move_left(mas), (res, 12))

    def test_12(self):
        mas = [[0, 0, 0, 0],
               [0, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        res = [[8, 0, 2, 2],
               [0, 0, 4, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        self.assertEqual(move_up(mas), (res, 8))

    def test_13(self):
        mas = [[2, 0, 2, 2],
               [2, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        res = [[4, 0, 4, 4],
               [8, 0, 4, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        self.assertEqual(move_up(mas), (res, 20))

    def test_14(self):
        mas = [[2, 0, 2, 2],
               [2, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [4, 0, 4, 0],
               [8, 0, 4, 4]]
        self.assertEqual(move_down(mas), (res, 20))

    def test_15(self):
        mas = [[2, 0, 2, 2],
               [2, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [4, 0, 4, 0],
               [8, 0, 4, 4]]
        self.assertEqual(move_down(mas), (res, 20))

    def test_16(self):
        mas = [[2, 0, 2, 2],
               [2, 0, 2, 2],
               [4, 0, 4, 0],
               [4, 0, 0, 0]]

        self.assertEqual(can_move(mas), True)

    def test_17(self):
        mas = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]

        self.assertEqual(can_move(mas), False)


if __name__=='main':
    unittest.main()