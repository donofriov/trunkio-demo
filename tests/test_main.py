import unittest
from src.main import greet

class TestMain(unittest.TestCase):

    def test_greet(self):
        args = "Vince"
        expected_result = "Hello, Vince!"
        self.assertEqual(greet(args), expected_result)

if __name__ == '__main__':
    unittest.main()
