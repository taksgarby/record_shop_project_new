import unittest
from models.genre import Genre

class TestGenre(unittest.TestCase):

    def setUp(self):
        self.genre = Genre("Jazz")

    def test_genre_has_name(self):
        self.assertEqual("Jazz", self.genre.genre_name)