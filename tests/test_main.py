import unittest
import time
from src.main import greet

class TestMain(unittest.TestCase):

    def test_greet(self):
        args = "Vince"
        expected_result = "Hello, Vince!"
        self.assertEqual(greet(args), expected_result)

    def test_long_running(self):
        time.sleep(180)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
