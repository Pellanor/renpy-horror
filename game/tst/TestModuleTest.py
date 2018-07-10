import unittest

import TestModule


class TestModuleTest(unittest.TestCase):

    def test_getRandom(self):
        self.assertEqual(4, TestModule.get_random_number())
