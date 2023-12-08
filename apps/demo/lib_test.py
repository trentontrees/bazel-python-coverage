import unittest
import numpy as np
from apps.demo.lib import DemoClass

class TestDemoClass(unittest.TestCase):
    def test_demo(self):
        d = DemoClass()
        got = d.demo()
        exp = "numpy demo: [2 4 6]"
        self.assertEqual(got, exp)

if __name__ == '__main__':
    unittest.main()
