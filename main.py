import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def chome():
    if request.method == "POST":
        url = "https://api.covid19api.com/summary"
        response = requests.get(url).json()
        lists = response.get("Countries")
        c = request.form["country"]
        for i in lists:
            if i["Country"].lower() == c.lower():
                data = {"name": i["Country"],
                        "confirmed": i["TotalConfirmed"],
                        "deaths": i["TotalDeaths"],
                        'code': 200}
                return render_template('home.html', data=data)
        else:
            data = {'message': 'Please Enter correct country', 'code': 404}
            return render_template('home.html', data=data)
    else:
        return render_template('home.html', data=None)


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(port=port)
