import physics as p
import unittest


class TestPhysics(unittest.TestCase):
    
    def test_calculate_buoyancy(self):
        self.assertEqual(p.calculate_buoyancy(1, 1),9.81)
    def test_will_it_float(self):
        self.assertTrue(p.will_it_float())
    def test_calculate_pressure(self):
        self.assertEqual
    def test_calculate_acceleration(self):
        self.assertEqual
    
    