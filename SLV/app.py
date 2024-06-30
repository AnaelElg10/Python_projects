from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', time=datetime.now(), title='Home', launches=launches)

@app.template_filter('datetime')
def deatetime_filter(s):
    date_object = datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%fZ')
    return date_object.date()

def fetch_spacex_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
    
def fetch_rocket_launches():
    url = 'https://launchlibrary.net/1.4/launch'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
    
launches = fetch_spacex_launches()

def categorize_launches(launches):
    successful_launches = list(filter(lambda launch: launch['success'] and not launch['upcoming'], launches))
    upcoming_launches = list(filter(lambda launch: launch['upcoming'], launches))
    failed_launches = list(filter(lambda launch: not launch['success'] and not launch['upcoming'], launches))

    return {
        'successful': successful_launches,
        'upcoming': upcoming_launches,
        'failed': failed_launches
    }

launches = categorize_launches(fetch_spacex_launches())

if __name__ == '__main__':
    app.run(debug=True)