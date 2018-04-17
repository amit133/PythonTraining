from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Flask App'

@app.route('/hello/<string:name>/')
def hello(name):
  return render_template('test.html', name = name)

if __name__ == '__main__':
  app.run(port=80)

