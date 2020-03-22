import requests
from flask import Flask, render_template, url_for, redirect, request, session, flash
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
Compress(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://corona.lmao.ninja/countries/india'
    r = requests.get(url).json()
    raju=[]
    raju=r
    country=raju['country']
    cases=raju['cases']
    deaths=raju['deaths']
    todayDeaths=raju['todayDeaths']
    todayCases=raju['todayCases']
    recovered=raju['recovered']
    activeCases=raju['active']
    percentDeath=int((deaths/cases)*100)
    percentRecovered=int((recovered/cases)*100)
    return render_template('index.html',country=country,cases=cases,deaths=deaths,todayDeaths=todayDeaths,recovered=recovered,active=activeCases,perDeath=percentDeath,todayCases=todayCases)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html"), 404


@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')
    
@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')
    
if __name__ == "__main__":
    # Development
    app.run(threaded=True, debug=True)

