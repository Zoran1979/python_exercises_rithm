from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus
from car import Car

cars = [Car("Toyota", "Corolla S", 2005), Car("Toyota", "Corolla S", 2005)]

app = Flask(__name__)
modus = Modus(app)


@app.route("/")
def root():
    return redirect(url_for('index'))


@app.route("/cars")
def index():
    return render_template("index.html", cars=cars)


@app.route("/cars/new")
def new():
    return render_template("new.html")


@app.route("/cars", methods=["POST"])
def create():
    make = request.form.get("car_make")
    model = request.form.get("car_model")
    year = request.form.get("car_year")
    cars.append(Car(make, model, year))
    return redirect(url_for("index"))


@app.route("/cars/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
    car = next(c for c in cars if c.id == int(id))
    if request.method == b"PATCH":
        car.make = request.form.get('car_make')
        car.model = request.form.get('car_model')
        car.year = request.form.get('car_year')
        return redirect(url_for("index"))
    if request.method == b"DELETE":
        cars.remove(car)
        return redirect(url_for('index'))
    return render_template("show.html", car=car)


@app.route(
    "/cars/<int:id>/edit", )
def edit(id):
    car = next(c for c in cars if c.id == int(id))
    return render_template('edit.html', car=car)


if __name__ == "__main__":
    app.run(debug=True, port=3000)