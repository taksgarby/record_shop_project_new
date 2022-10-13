from db.run_sql import run_sql

from models.artist import Artist
from models.genre import Genre
from models.record import Record

def save(genre):
    sql = "INSERT INTO genres (genre_name) VALUES (%s) RETURNING *"
    values = [genre.genre_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    genre.id = id
    return genre


def select_all():
    genres = []

    sql = "SELECT * FROM genres"
    results = run_sql(sql)

    for row in results:
        genre = Genre(row['genre_name'], row['id'] )
        genres.append(genre)
    return genres


def select(id):
    genre = None
    sql = "SELECT * FROM genres WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        genre = Genre(result['genre_name'], result['id'] )
    return genre


def delete_all():
    sql = "DELETE  FROM genres"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM genres WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(genre):
    sql = "UPDATE genres SET (genre_name) = (%s) WHERE id = %s"
    values = [genre.genre_name, genre.id]
    run_sql(sql, values)



def records(genre):
    records = []

    sql = "SELECT * FROM records WHERE genre_id = %s"
    values = [genre.id]
    results = run_sql(sql, values)

    for row in results:
        record = Record(row['title'], row['artist'], row['genre_id'], row['year'], row['buying_cost'], row['price'], row['stock_count'], row['id'])
        records.append(record)
    return records
