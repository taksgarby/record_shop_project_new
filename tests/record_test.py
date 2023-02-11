import unittest
from models.record import Record

class TestRecord(unittest.TestCase):

    def setUp(self):
        self.record = Record("Plan", "Death Cab for Cutie", "Rock & Pop", 2001, 30, 10.05, 20.50, 10)
    
    def test_record_has_title(self):
        self.assertEqual("Plan", self.record.title)

    def test_record_has_artist(self):
        self.assertEqual("Death Cab for Cutie", self.record.artist)
    
    def test_record_has_genre(self):
        self.assertEqual("Rock & Pop", self.record.genre)
    
    def test_record_has_year(self):
        self.assertEqual(2001, self.record.year)

    def test_record_has_stock_count(self):
        self.assertEqual(30, self.record.stock_count)
    
    def test_record_has_buying_cost(self):
        self.assertEqual(10.05, self.record.buying_cost)
    
    def test_record_has_price(self):
        self.assertEqual(20.50, self.record.price)

    def test_record_has_id(self):
        self.assertEqual(10, self.record.id)