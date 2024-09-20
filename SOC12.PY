def subtract(a,b):
    return (a-b)

import unittest

class loginclass(unittest.TestCase):
    def test1(self):
        result = subtract(10,7)
        self.assertEqual(result,3)
        
    def test2(self):
        result = subtract(10,-3)
        self.assertEqual(result,13)

    def test3(self):
        result = subtract(-10,3)
        self.assertEqual(result,-13)

    def test4(self):
        result = subtract(10,-7)
        self.assertEqual(result,17)

    def test5(self):
        result = subtract(-10,7)
        self.assertEqual(result,-17)

if __name__ == '__main__':
    unittest.main()
