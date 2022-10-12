from db.run_sql import run_sql

from models.artist import Artist
from models.record import Record

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name, country) VALUES (%s, %s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name, artist.country]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists order by last_name"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['first_name'], row['last_name'], row['country'], row['id'] )
        artists.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['first_name'], result['last_name'], result['country'], result['id'] )
    return artist


def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (first_name, last_name, country) = (%s, %s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.country, artist.id]
    run_sql(sql, values)



def records(artist):
    records = []

    sql = "SELECT * FROM records WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        record = Record(row['title'], row['artist_id'], row['genre'], row['year'], row['buying_cost'], row['price'], row['stock_count'], row['id'])
        records.append(record)
    return records
