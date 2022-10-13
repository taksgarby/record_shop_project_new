from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
from models.genre import Genre
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository
import repositories.genre_repository as genre_repository


genres_blueprint= Blueprint("genres", __name__)

@genres_blueprint.route("/genres")
def genres():
    genres = genre_repository.select_all()
    return render_template("genres/index.html", all_genres = genres)

# create a new genre form
@genres_blueprint.route("/genres/add", methods= ['GET'])
def add_genre():
    return render_template("genres/add.html")

# create a new genre
@genres_blueprint.route("/genres", methods=['POST'])
def create_genre():
    genre_name = request.form['genre_name']
    genre = Genre(genre_name)
    genre_repository.save(genre)
    return redirect('genres')


@genres_blueprint.route("/genres/<id>", methods=['GET'])
def show_genre(id):

    return render_template('genres/show.html', genre = genre_repository.select(id), all_records = record_repository.select_all())

# @genres_blueprint.route("/genres/<genre_name>", methods=['GET'])
# def show_genre(genre_name):
#     return render_template('genres/show.html',
#     genre_name = record_repository.select(genre),
#     all_records = record_repository.select_all())
