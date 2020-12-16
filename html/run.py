from flask import Flask, render_template, session, make_response, url_for, redirect, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
  return render_template('test.html',name = '사용자명')

@app.route('/news')
def home():
  return render_template('test.html',name = '사용자명')

@app.route('/index')
def home():
  return render_template('test.html',name = '사용자명')

@app.route('/exchange')
def home():
  return render_template('test.html',name = '사용자명')

@app.route('/videos')
def home():
  return render_template('test.html',name = '사용자명')



if __name__=='__main__':
  app.run(debug=True)