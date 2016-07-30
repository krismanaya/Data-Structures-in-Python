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
        self.assertTrue(False)

    def test_distinct_numbers(self):
        expected = False
        actual = Homework.distinct_numbers([1,2,3,4,5]) 
        self.assertEqual(expected,actual)

