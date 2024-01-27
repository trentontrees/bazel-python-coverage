import unittest
from apps.demo.lib import DemoClass

class TestDemoClass(unittest.TestCase):
    def test_demo(self):
        d = DemoClass()
        got = d.demo()
        exp = "demo time"
        self.assertEqual(got, exp)

if __name__ == '__main__':
    unittest.main()
