from flask import Flask
app = Flask(__name__)
@app.route('/') # 'http://www.google.com/'
def home():
    return "Hello, flask app"

@app.route('/myindex') # 'http://www.google.com/'
def myindex():
    return "Hello, flask app home"

app.run(port=5000)