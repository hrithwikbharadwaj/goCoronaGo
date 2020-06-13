import requests
from flask import Flask, render_template, url_for, redirect, request, session, flash
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
from flask_sslify import SSLify
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
sslify = SSLify(app)
Compress(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://api.covid19india.org/data.json'
    r = requests.get(url).json()
    cases=r['statewise']
    list1=cases[0]
    raju=list1
    
    cases=raju['confirmed']
    deaths=raju['deaths']
    
    recovered=raju['recovered']
    activeCases=raju['active']
    latest=raju['lastupdatedtime']
    url2= 'https://v1.api.covindia.com/district-values'
    b = requests.get(url2).json()
# print(r)
    n=len(r)
    dis=[]
    others=[]
# print(r[0])
    for x, y in b.items():
        dis.append(x)
        others.append(y)
    
    return render_template('index.html',cases=cases,deaths=deaths,recovered=recovered,active=activeCases,latest=latest,dis=dis,others=others)

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
    # http_server = WSGIServer(('', 8080), app)
    # http_server.serve_forever()

