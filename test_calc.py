import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual (calc.add(5, 5), 10)
        self.assertEqual (calc.add(10, 10), 20)


    def test_substract(self):
        
        self.assertEqual (calc.substract(5, 5), 0)
        self.assertEqual (calc.substract(8, 4), 4)

    def test_multiply(self):
        
        self.assertEqual (calc.multiply(3, 4), 12)
        self.assertEqual (calc.multiply(10, 2), 20)

    def test_divide(self):
        
        self.assertEqual (calc.divide(40, 5), 8)
        self.assertEqual (calc.divide(10, 10), 1)



if __name__ == '__main__':
    unittest.main()