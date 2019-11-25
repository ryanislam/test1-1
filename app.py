
from flask import Flask, url_for, render_template, request


app = Flask(__name__)
app.secret_key = 'fbd1eefad885bf835e1d5ea884244221'

@app.errorhandler(404)
def err_404(error):
   return render_template( '404.html' ), 404

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
  return render_template('index.html', title='Home')


@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/table_example')
def table_example():
  return render_template('table_example.html', title='Data Table')


@app.route('/login')
def login():
  return render_template('login.html', title='Login')


@app.route('/handle_data', methods=['GET','POST'])
def handle_data():
  us = request.form['username']
  pw = request.form['password']

  return render_template('index.html', 
    title='Home', 
    msg=f"{us} is registered {pw}",
    msg_class= "alert alert-success")


# print("-- DEBUG MODE ----")
# app.run(debug=True, port='5555')

import os
from waitress import serve

print("--PRODUCTION MODE ---")
p = os.environ.get('PORT')
serve(app, host='0.0.0.0', port=p)


