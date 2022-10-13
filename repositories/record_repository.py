from db.run_sql import run_sql

from models.record import Record
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.genre_repository as genre_repository

def save(record):
    sql = "INSERT INTO records (title, artist_id, genre_id, year, stock_count, buying_cost, price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [record.title, record.artist.id, record.genre.id, record.year, record.stock_count, record.buying_cost, record.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    record.id = id
    return record

def select_all():
    records = []

    sql = "SELECT * FROM records"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        genre = genre_repository.select(row['genre_id'])
        record = Record(row['title'], artist, genre, row['year'], row['stock_count'], row['buying_cost'], row['price'], row['id'])
        records.append(record)
    return records

def select(id):
    record = None
    sql = "SELECT * FROM records WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        genre = genre_repository.select(row['genre_id'])
        record = Record(result['title'], artist, genre, result['year'],  result['stock_count'], result['buying_cost'], result['price'], result['id'] )
    return record


def delete(id):
    sql = "DELETE  FROM records WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(record):

    sql = "UPDATE records SET (title, artist_id, genre_id, year, stock_count, buying_cost, price) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    
    values = [record.title, record.artist.id, record.genre.id, record.year, record.stock_count,  record.buying_cost, record.price, record.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM records"
    run_sql(sql)