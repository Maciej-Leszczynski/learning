import unittest
from lp3_analyser import Lp3DataAnalyser

class TestLp3DataAnalyser(unittest.TestCase):
    def test_instance_creation(self):
        charts = Lp3DataAnalyser("lp3_2018.csv")
        self.assertIsInstance(charts, Lp3DataAnalyser)

if __name__ == "__main__":
    unittest.main()