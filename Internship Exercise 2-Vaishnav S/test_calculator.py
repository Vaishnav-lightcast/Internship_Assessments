import unittest
import calculator
class Testcalculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(5, 6)
        self.assertEqual(result, 11)           #TC1
        
        result = calculator.add(-7, -6)
        self.assertEqual(result, -13)          #TC2
        
        result = calculator.add(-5, 6)
        self.assertEqual(result, 1)            #TC3
        
        result = calculator.add(5, 0)
        self.assertEqual(result, 5)            #TC4
        
    def test_subtract(self):
        result = calculator.subtract(5, 6)
        self.assertEqual(result, -1)           #TC5

        result = calculator.subtract(-5, -6)
        self.assertEqual(result, 1)            #TC6

        result = calculator.subtract(8, -6)
        self.assertEqual(result, 14)           #TC7
        
    def test_multiply(self):
        result = calculator.multiply(5, 5)
        self.assertEqual(result, 25)           #TC8

        result = calculator.multiply(-5, -6)
        self.assertEqual(result, 30)           #TC9

        result = calculator.multiply(5, -6)
        self.assertEqual(result, -30)           #TC10

        result = calculator.multiply(8, 0)
        self.assertEqual(result, 0)             #TC11
        
    def test_division(self):
        result = calculator.division(8, 4)
        self.assertEqual(result, 2)             #TC12
        
        with self.assertRaises(ValueError):
            calculator.division(5, 0)           #TC13
            
        result = calculator.division(0, 5)
        self.assertEqual(result, 0)             #TC14
            
    def test_mod(self):
        result = calculator.mod(8, 4)
        self.assertEqual(result, 0)             #TC15
        
        with self.assertRaises(ValueError):
            calculator.mod(10, 0)               #TC16

        result = calculator.mod(0, 4)
        self.assertEqual(result, 0)             #TC17

if __name__ == '__main__':
         unittest.main()
