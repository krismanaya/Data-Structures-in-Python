import unittest
import random
import Homework 

class HomeworkSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_exponentiate(self):
        expected = [1,2,4,8,16,32,64,128,256]
        actual = Homework.power_of_two(9)
        self.assertEqual(expected,actual)

    def test_choice(self):
        pass

    def test_distinct_numbers(self):
        expected = True
        actual = Homework.distinct_numbers([1,2,3,4,5]) 
        self.assertEqual(expected,actual)
        expected_1 = False 
        actual = Homework.distinct_numbers([1,1,2,3,4,5])
        self.assertEqual(expected_1,actual)
        expected_2 = False 
        actual = Homework.distinct_numbers([1,2,2,3,4,5])
        self.assertEqual(expected_2,actual)


    def test_alphabet(self):
        expected = ['a','b','c','d','e','f','g','h','i','j',
                    'k','l','m','n','o','p','q','r','s','t',
                    'u','v','w','x','y','z']
        actual = Homework.alphabet()
        self.assertEqual(expected,actual)

    def test_count_vowel(self): 
        expected = 31
        actual = Homework.count_vowel('If I have seen farther then other men, it is because I have stood on the shoulders of giants.')
        self.assertEqual(expected,actual)

    def test_factors_modify(self): 
        expected = [1, 2, 5, 10]
        def factors_modify(): 
            return [i for i in Homework.factors_modify(10)]
        self.assertEqual(expected, factors_modify())

    def test_polynomial(self):
        """to pass this test please enter 12*x**2 + 2*x -5 and 2 for the input"""
        expected = 1.0000000000065512
        actual = Homework.main() 
        self.assertEqual(expected,actual)

