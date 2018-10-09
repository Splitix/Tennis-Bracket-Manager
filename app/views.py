from flask import render_template, request
from app import app
from app.forms import FormNames, Generator
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

@app.route('/')
def hello_world():
	form = FormNames()
	return render_template('index.html', form = form)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['names']
    processed_text = text.upper()
    players = Generator().playerNames(processed_text)
    print(players)
    return render_template('helloWorld.html', players = players)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    form = FormNames()
    return render_template("result.html",form = form)
