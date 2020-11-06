import calculator1
import unittest

 


class TestCalculator(unittest.TestCase):

 

    def test_addition(self):
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)
        print("asserion addition complete")
        

 

    def test_subtraction(self):
        result = calculator.subtract(4,2)
        self.assertEqual(result, 2)
        print("asserion substraction complete")
        
        
if __name__ == '__main__':
    unittest.main()
