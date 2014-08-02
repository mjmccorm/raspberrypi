#https://docs.python.org/2/library/unittest.html

import test_function
import unittest

class exampleTests(unittest.TestCase):

    #def setUp(self):
        #nothing to setup

    #tests begin with test    
    #
    #test_1 should fail
    #def test_1(self):
    #        self.assertEqual(test_function.stradd("a","b"),"ac")

    def test_2(self):
            self.assertEqual(test_function.stradd("a","c"),"ac")

    def test_3(self):
            self.assertTrue(test_function.stradd("a","c") != "")
    

if __name__ == "__main__":
        unittest.main()
