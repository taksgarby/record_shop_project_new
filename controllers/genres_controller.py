from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


genres_blueprint= Blueprint("genres", __name__)

@genres_blueprint.route("/genres/add")
def add_genre():
    return render_template("genres/add.html")

@genres_blueprint.route("/genres")
def genres():
    records = record_repository.select_all()
    return render_template("genres/index.html", all_records = records)

# @genres_blueprint.route("/genres/<genre_name>", methods=['GET'])
# def show_genre(genre_name):
#     return render_template('genres/show.html',
#     genre_name = record_repository.select(genre),
#     all_records = record_repository.select_all())
