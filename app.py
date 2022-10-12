from flask import Flask, render_template

from controllers.records_controller import records_blueprint
from controllers.artists_controller import artists_blueprint
from controllers.genres_controller import genres_blueprint

from repositories import record_repository


app = Flask(__name__)

app.register_blueprint(records_blueprint)
app.register_blueprint(artists_blueprint)
app.register_blueprint(genres_blueprint)

@app.route('/')
def home():
    records = record_repository.select_all()
    return render_template('home.html', all_records = records)

if __name__ == '__main__':
    app.run(debug=True)