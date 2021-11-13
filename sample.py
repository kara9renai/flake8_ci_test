import unittest


def add(a, b):
    return a+b


class TestAdd(unittest.TestCase):
    def testaddfunc(self):
        val1 = 2
        val2 = 3
        expected = 5
        self.assertEqual(add(val1, val2),  expected)


if __name__ == '__main__':
    unittest.main()
