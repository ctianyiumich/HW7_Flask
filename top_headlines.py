from flask import Flask, render_template
import json
import secrets
import requests
api_url= f"https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={secrets.api_key}"
hl_list = []
response = requests.get(api_url)
nytimes_dict = json.loads(response.text)
for result in nytimes_dict['results'][:5]:
    hl_list.append(result)

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/Buffy')
def name():
    return render_template('name.html', name = "Buffy", headlines_list = hl_list)

if __name__ == '__main__':

    app.run(debug=True)
