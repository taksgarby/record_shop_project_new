
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record import Record
from models.artist import Artist
import repositories.record_repository as record_repository
import repositories.artist_repository as artist_repository


artists_blueprint= Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", all_artists = artists)

# create a new artist form
@artists_blueprint.route("/artists/add", methods= ['GET'])
def add_artist():
    
    return render_template("artists/add.html")

# create a new artist
@artists_blueprint.route("/artists", methods=['POST'])
def create_artist():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    country = request.form['country']
    artist = Artist(first_name, last_name, country)
    artist_repository.save(artist)
    return redirect('/artists')


# show artist details
@artists_blueprint.route("/artists/<id>", methods=['GET'])
def show_artist(id):

    return render_template('artists/show.html', artist = artist_repository.select(id), all_records = record_repository.select_all())

# edit
@artists_blueprint.route("/artists/<id>/edit", methods=['GET'])
def edit_artist(id):
    return render_template('artists/edit.html',
                            artist = artist_repository.select(id),
                            all_records = record_repository.select_all())


# update artist
@artists_blueprint.route("/artists/<id>", methods=['POST'])
def update_artist(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    country = request.form['country']
    artist = Artist(first_name, last_name, country, id)
    artist_repository.update(artist)
    return redirect('/artists')

