from flask import Flask, render_template
import data as tours


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def torus(id):
    return render_template('tour.html')


@app.route('/data/')
def data():
    article = 'все туры:'
    return render_template('data.html', article=article, tours=tours.tours, )


@app.route('/data/departures/<departure>')
def data_dep(departure):
    article = 'Туры по направлению ' + tours.departures[departure] + ':'
    filtered_tours = {}
    for tour in tours.tours:
        if departure in tours.tours[tour].values():
            filtered_tours[tour] = tours.tours[tour]
    return render_template('data.html', article=article, tours=filtered_tours)


@app.route('/data/tours/<id>')
def data_id(id):
    return render_template('data_tour.html', tour=tours.tours[int(id)])


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


@app.errorhandler(404)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error.original_exception), 404


app.run()
