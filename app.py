from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def hello_world():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1

    if session['counter'] % 2 == 0:
        return "World"
    else:
        return "Hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
