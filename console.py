import pdb
from models.artist import Artist
from models.genre import Genre
from models.record import Record

import repositories.artist_repository as artist_repository
import repositories.genre_repository as genre_repository
import repositories.record_repository as record_repository

record_repository.delete_all()
genre_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Joni', 'Mitchell', 'Canada')
artist_repository.save(artist1)

artist2 = Artist('Fiona', 'Apple', 'USA')
artist_repository.save(artist2)

artist3 = Artist('John', 'Coltrane', 'USA')
artist_repository.save(artist3)

artist4 = Artist('Henri', 'Salvador', 'France')
artist_repository.save(artist4)

artist5 = Artist('John', 'Williams', 'USA')
artist_repository.save(artist5)

artist6 = Artist('Hans', 'Zimmer', 'Germany')
artist_repository.save(artist6)

genre1 = Genre('Folk')
genre_repository.save(genre1)

genre2 = Genre('Classical')
genre_repository.save(genre2)

genre3 = Genre('Rock & Pop')
genre_repository.save(genre3)

genre4 = Genre('Soundtrack')
genre_repository.save(genre4)

genre5 = Genre('Jazz')
genre_repository.save(genre5)

record1 = Record('Blue', artist1, genre1, 1971, 5, 15.00, 30.00)
record_repository.save(record1)

record2 = Record('Extraordinary Machine', artist2, genre3 , 2005, 2, 10.50, 20.00)
record_repository.save(record2)

record3 = Record('Room With A View', artist4, genre5, 2000, 1, 13.50, 25.00)
record_repository.save(record3)

record4 = Record('Blue Train', artist3, genre5 , 2022, 10, 15.50, 35.00)
record_repository.save(record4)

record5 = Record('Both Sides Now', artist1, genre1 , 1969, 3, 12.00, 25.00)
record_repository.save(record5)

record6 = Record('Jurassic Park Theme', artist5, genre4 , 1995, 10, 13.00, 28.00)
record_repository.save(record6)

record7 = Record('The Star Wars Theme', artist5, genre4 , 1985, 10, 10.00, 18.00)
record_repository.save(record7)

record8 = Record('The Inception Theme', artist6, genre4 , 2010, 15, 12.00, 24.00)
record_repository.save(record8)

record9 = Record('The Intersteller Theme', artist6, genre4 , 2015, 2, 13.00, 25.00)
record_repository.save(record9)




# record1 = Record('Blue', artist1, 'Folk', 1971, 5, 15.00, 30.00)
# record_repository.save(record1)

# record2 = Record('Extraordinary Machine', artist2, 'Pop & Rock', 2005, 2, 10.50, 20.00)
# record_repository.save(record2)

# record3 = Record('Room With A View', artist4, 'Jazz', 2000, 1, 13.50, 25.00)
# record_repository.save(record3)

# record4 = Record('Blue Train', artist3, 'Jazz', 2022, 10, 15.50, 35.00)
# record_repository.save(record4)

# record5 = Record('Both Sides Now', artist1, 'Folk', 1969, 3, 12.00, 25.00)
# record_repository.save(record5)

# record6 = Record('Jurassic Park Theme', artist5, 'Soundtrack', 1995, 10, 13.00, 28.00)
# record_repository.save(record6)

# record7 = Record('The Star Wars Theme', artist5, 'Soundtrack', 1985, 10, 10.00, 18.00)
# record_repository.save(record7)

# record8 = Record('The Inception Theme', artist6, 'Soundtrack', 2010, 15, 12.00, 24.00)
# record_repository.save(record8)

# record9 = Record('The Intersteller Theme', artist6, 'Soundtrack', 2015, 2, 13.00, 25.00)
# record_repository.save(record9)


