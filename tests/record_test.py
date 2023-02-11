import unittest
from models.record import Record

class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record("Plan", "Death Cab for Cutie", "Rock & Pop", 2001, 30, 10.05, 20.50, 10)
    
    def test_record_has_title(self):
        self.assertEqual("Plan", self.record.title)

    def test_record_has_artist(self):
        self.assertEqual("Death Cab for Cutie", self.record.artist)