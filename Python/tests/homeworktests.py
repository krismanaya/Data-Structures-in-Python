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
