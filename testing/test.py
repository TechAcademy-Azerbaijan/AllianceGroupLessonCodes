import unittest

from main import Calc


class TestMathOpetation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup')
        a = 2
        b = 4
        cls.calc = Calc(a, b)
        a = -4
        b = 0
        cls.calc2 = Calc(a, b)

    def test_add(self):
        print('test_add')
        expected_result = 6
        actual_result = self.calc.add()

        # assert actual_result == expected_result
        self.assertEqual(actual_result, expected_result)

#    def test_add2(self):
#        print('test_add2')
#        expected_result = 7
#        actual_result = self.calc.add()

#        self.assertEqual(actual_result, expected_result)

    def test_divide(self):
        print('test_divide')
        expected_result = 0.5
        actual_result = self.calc.divide()
        self.assertEqual(actual_result, expected_result)

    def test_divide2(self):
        print('test_divide2')
        self.assertRaises(ZeroDivisionError, self.calc2.divide)
    
    @classmethod
    def tearDownClass(cls):
        print('tearDown')
    


if __name__ == '__main__':
    unittest.main()