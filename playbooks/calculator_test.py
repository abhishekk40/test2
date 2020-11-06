import calculator1
import unittest

 


class TestCalculator(unittest.TestCase):

 

    def test_addition(self):
        result = calculator.add(1, 2)
        self.assertEqual(result, 4)
        print("addition assertion completed")
        

 

    def test_subtraction(self):
        result = calculator.subtract(4,2)
        self.assertEqual(result, 2)
        print("substraction assertion completed")
        
        
if __name__ == '__main__':
    unittest.main()
