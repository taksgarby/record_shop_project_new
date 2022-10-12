import pdb
from models.artist import Artist
from models.record import Record

import repositories.artist_repository as artist_repository
import repositories.record_repository as record_repository

record_repository.delete_all()
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




record1 = Record('Blue', artist1, 'Folk', 1971, 5, 15.00, 30.00)
record_repository.save(record1)

record2 = Record('Extraordinary Machine', artist2, 'Pop & Rock', 2005, 2, 10.50, 20.00)
record_repository.save(record2)

record3 = Record('Room With A View', artist4, 'Jazz', 2000, 1, 13.50, 25.00)
record_repository.save(record3)

record4 = Record('Blue Train', artist3, 'Jazz', 2022, 10, 15.50, 35.00)
record_repository.save(record4)

record5 = Record('Both Sides Now', artist1, 'Folk', 1969, 3, 12.00, 25.00)
record_repository.save(record5)

record6 = Record('Jurassic Park Theme', artist5, 'Soundtrack', 1995, 10, 13.00, 28.00)
record_repository.save(record6)

record7 = Record('The Star Wars Theme', artist5, 'Soundtrack', 1985, 10, 10.00, 18.00)
record_repository.save(record7)

record8 = Record('The Inception Theme', artist6, 'Soundtrack', 2010, 15, 12.00, 24.00)
record_repository.save(record8)

record9 = Record('The Intersteller Theme', artist6, 'Soundtrack', 2015, 2, 13.00, 25.00)
record_repository.save(record9)


