import unittest
import random
from anagram import is_anagram

"""
Using Python's built-in unittest framework, any member function whose name begins
with test in a class deriving from unittest.TestCase will be run, and its assertions
checked, when unittest.main() is called.

"""
class AnagramTestCase(unittest.TestCase):
    """ Collections of tests for is_anagram method"""

    # The TestCase class provides several assert methods to check for and report
    # failures. "assert" literally means, "to state as fact", the most common:
    # -----------------------------------
    # METHOD                    Check if
    # -----------------------------------
    # assertEqual(a, b)         a == b
    # assertNotEqual(a, b)      a != b
    # assertTrue(x)	bool(x)     is True
    # assertFalse(x)            bool(x) is False
    # assertIs(a, b)            a is b
    # assertIsNot(a, b)         a is not b
    # assertIsNone(x)           x is None
    # assertIsNotNone(x)        x is not None
    # assertIn(a, b)            a in b
    # assertNotIn(a, b)         a not in b
    # assertIsInstance(a, b)    isinstance(a, b)
    # assertNotIsInstance(a, b) not isinstance(a, b)

    # Each test should test a single, specific property of the code
    # and be name accordingly
    def test_is_anagram(self):
        self.assertTrue(is_anagram("casa", "asac"))

    def test_is_not_anagram(self):
        self.assertFalse(is_anagram("window", "water"))

    # Calling a test method in a loop is perfectly valid, you can
    # now the one that failed using the msg parameter
    def test_random_anagram_n_strings(self):
        for i in range(20):
            astring = self.generate_random_string(30)
            astring_shuffled = self.shuffle_string(astring)
            self.assertTrue(is_anagram(astring,astring_shuffled),msg='{} was the input string'.format(astring))

    # Test always the boundaries of your logic and how it handles uncommon
    # input. You need to know clearly the spec for these situations in order
    # to write the correct assert.
    def test_is_empty_string(self):
        self.assertTrue(is_anagram("",""))

    def test_is_input_none(self):
        self.assertFalse(is_anagram(None, "abc"))

    # You can have accessory functions for the TestCase that will no be run
    # as a test case if they do not start with test_
    def generate_random_string(self, length):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join([random.choice(alphabet) for i in range(length)])

    def shuffle_string(self, astring):
        l = list(astring)
        random.shuffle(l)
        return ''.join(l)

if __name__ == '__main__':
    unittest.main()
