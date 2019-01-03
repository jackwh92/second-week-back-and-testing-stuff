import unittest
from firstweek import function

class theclass(unittest.TestCase):

    def test_totestaaddsb(self):
        self.assertEqual(function(2,3), (5))

if __name__=="__main__":
    unittest.main()