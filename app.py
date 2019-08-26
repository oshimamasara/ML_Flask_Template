from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/calc',methods=['POST'])
def calc():
    stores = int(request.form['store'])
    url = 'http://0.0.0.0:5555/api'
    r = requests.post(url,json={'exp':stores})
    x = round(r.json())
    return render_template('output.html',calc = x)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)