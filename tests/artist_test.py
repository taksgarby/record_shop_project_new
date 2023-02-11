import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Miles", "Davis", "USA", 10)

    def test_artist_has_first_name(self):
        self.assertEqual("Miles", self.artist.first_name)
    
    def test_artist_has_last_name(self):
        self.assertEqual("Davis", self.artist.last_name)