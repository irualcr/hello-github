import unittest

from hellogit import main, message

class TestHelloGit(unittest.TestCase):
    def test_message(self):
        self.assertEqual(message("Laure"), "Hello, Laure")

    def test_main(self):
        self.assertEqual(main("Laure"), "Hello, Laure")

if __name__ == "__main__":
    unittest.main()