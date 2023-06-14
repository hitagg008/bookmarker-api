import unittest
import src.app as app

class TestApp(unittest.TestCase):
    def test_hello(self):
        response = app.index()
        self.assertEqual(response, 'Hello World')

if __name__ == '__main__':
    unittest.main()
