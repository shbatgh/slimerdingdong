from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    return render_template('buy.html')

@app.route('/20798123592375')
def hello():
    return render_template("conno.html")


if __name__ == '__main__':
    app.run(debug=True)
