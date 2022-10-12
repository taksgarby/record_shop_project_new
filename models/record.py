class Record:
    def __init__(self, title, artist, genre, year, stock_count, buying_cost, price, id = None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year
        self.stock_count = stock_count
        self.buying_cost = buying_cost
        self.price = price
        self.id = id
       

    def markup(self):
        return self.price - self.buying_cost