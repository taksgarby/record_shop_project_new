
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
from models.artist import Artist
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


records_blueprint= Blueprint("records", __name__)

@records_blueprint.route("/records")
def records():
    records = record_repository.select_all()
    return render_template("records/index.html", all_records = records)

@records_blueprint.route("/add", methods= ['GET'])
def add():
    return render_template("add.html", all_artists = artist_repository.select_all())


@records_blueprint.route("/records", methods=['POST'])
def create_record():
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    stock_count = request.form['stock_count']
    buying_cost = request.form['buying_cost']
    price = request.form['price']
    artist_id = request.form['artist_id']
    artist = artist_repository.select(artist_id)
    record = Record(title, artist, genre, year, stock_count, buying_cost, price)
    record_repository.save(record)
    return redirect('/records')


@records_blueprint.route("/records/<id>", methods=['GET'])
def show_record(id):
    return render_template('records/show.html', record = record_repository.select(id))


@records_blueprint.route("/records/<id>/edit", methods=['GET'])
def edit_record(id):
    return render_template('records/edit.html',
                            record = record_repository.select(id),
                            all_artists = artist_repository.select_all())


@records_blueprint.route("/records/<id>", methods=['POST'])
def update_record(id):
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    stock_count = request.form['stock_count']
    buying_cost = request.form['buying_cost']
    price = request.form['price']
    artist_id = request.form['artist_id']
    artist = artist_repository.select(artist_id)
    record = Record(title, artist, genre, year, stock_count, buying_cost, price, id)
    record_repository.update(record)
    return redirect('/records')

