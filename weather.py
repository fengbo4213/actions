#!/usr/bin/env python3

from flask import Flask
from flask import request
import requests

app = Flask(__name__)

key = "57ec79d679004745aa65c283c3775ed4"

@app.route("/city/<province>/<city>")
def getCity(province, city):
    url = "https://geoapi.heweather.net/v2/city/lookup?key=%(key)s&location=%(city)s&adm=%(province)s" % {"key": key, "city": city, "province": province}
    r = requests.get(url)
    return r.text

@app.route("/weather/<location>")
def getWeather(location):
    url = "https://devapi.heweather.net/v7/weather/now?key=%(key)s&location=%(location)s" % {"key": key, "location": location}
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)