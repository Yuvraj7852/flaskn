from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


data = np.array([
    [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
    [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]
])

salary_data = np.array([40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000])


model = LinearRegression()
model.fit(data, salary_data)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        try:
            experience = float(request.form["experience"])
            io_level = float(request.form["io_level"])
        except ValueError:

            return render_template("index.html", error="Please enter valid numbers.")

        #
        predicted_salary = model.predict([[experience, io_level]])[0]

        return render_template("index.html", salary=predicted_salary, experience=experience, io_level=io_level)

    return render_template("index.html", salary=None)


if __name__ == "__main__":
    app.run(debug=True)

