import unittest
import tests.testExample
import tests.homeworktests

def suite():
    s = unittest.TestSuite()

    s.addTest(unittest.makeSuite(tests.testExample.TestSequenceFunctions))
    s.addTest(unittest.makeSuite(tests.homeworktests.HomeworkSequenceFunctions))

    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
