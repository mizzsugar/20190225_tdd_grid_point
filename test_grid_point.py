import unittest


class GridPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x},{y})'.format(x=self.x, y=self.y)


class TestGridPoint(unittest.TestCase):
    def test_課題1_1(self):
        grid_point = GridPoint(4, 7)

        with self.subTest('格子点はx座標を持つ'):
            self.assertEqual(4, grid_point.x)

        with self.subTest('格子点はy座標を持つ'):
            self.assertEqual(7, grid_point.y)

        with self.subTest('格子点から文字列表記を取得できる'):
            self.assertEqual('(4,7)', str(grid_point))


if __name__ == '__main__':
    unittest.main()
