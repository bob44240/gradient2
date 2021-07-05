from my_project import analysis

import unittest

class TestTrain(unittest.TestCase):

    def test_training_returns_True(self):
        self.assertEqual(analysis.run(), True)

if __name__ == '__main__':
    unittest.main()
