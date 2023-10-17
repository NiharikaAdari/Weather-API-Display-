from flask import Flask, render_template, request, make_response
from weather import main as get_weather

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def index():
    data = None
    measurement = None
    
    if 'temperatureUnit' in request.cookies:
        measurement = request.cookies.get('temperatureUnit')

    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        measurement = request.form['temperatureUnit']
        
        #set cookie
        response = make_response(render_template('index.html', data=data, measurement=measurement))
        response.set_cookie('temperatureUnit', measurement)

        data = get_weather(city, state, country, measurement)

    return render_template('index.html', data=data, measurement=measurement)

if __name__ == '__main__':
    app.run(debug=True)