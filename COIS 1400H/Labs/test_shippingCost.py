import unittest
import shippingCost

class TestShippingCost(unittest.TestCase):

    #first test case
    #Greater than 10; weight = 10
    def test_shippingCostA(self):
        result = shippingCost.calculateCost(11)
        self.assertEqual(result, 4.75)

#Adding all other test cases for the rest of the if else branches

    #second test case
    #Greater than 6; weight = 9
    def test_shippingCostB(self):
        result = shippingCost.calculateCost(9)
        self.assertEqual(result, 4.00)

    #third test case
    #greater than 2; weight = 2
    def test_shippingCostC(self):
        result = shippingCost.calculateCost(5)
        self.assertEqual(result, 3.00)

    #fourth test case
    #less than equal to; weight = 2
    def test_shippingCostD(self):
        result = shippingCost.calculateCost(2)
        self.assertEqual(result, 1.50)

#check for failures
#there is no account of negative input, upon sending a negative weight,
# there should be printed "Error" but instead it returns the value from
# the else statement. This is the check for failure. 
    def test_shippingCostFail(self):
        result = shippingCost.calculateCost(-2)
        self.assertEqual(result, "Error")


#run with -             
#python3.8 -m unittest test_shippingCost.py
#python/py would give error in cd, python3.8 is what works

    #Output
    #As the screenhsot depicts, there were 5 test cases run
    # 1 of them fialed - check for failure test case
    # others all passed
    #but since one of them failed, therefore, the total result was 'F'

    #Also, IDLE has space indentation errors, so need to be careful with that. 
    
