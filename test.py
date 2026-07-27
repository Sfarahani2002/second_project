import unittest 
from test_count import countm

class TestCountM(unittest.TestCase):
    def test_simple(self):
        s = "mohammad"
        a = 'm' 
        self.assertEqual(countm(s, a), 3)
    
    def test_nothing(self):
        s = ""
        a = "p" 
        self.assertEqual(countm(s, a), 0)
        
    def test_longer(self):
        s = "mohammad mohammadi"
        a = "m"
        self.assertEqual(countm(s, a), 6)
        
    def test_non_existence(self):
        s = "mohammad"
        a = "s"
        self.assertEqual(countm(s, a), 0)
        
if __name__ == '__main__':
    unittest.main()