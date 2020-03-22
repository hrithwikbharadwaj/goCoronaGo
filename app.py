import requests
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
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
   

        


    

if __name__ == "__main__":
    # Development
    # app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
