from flask import Flask


'''__name__ = main'''
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'PÁGINA SOBRE'


if __name__ == '__main__':
    app.run(debug=True) 
