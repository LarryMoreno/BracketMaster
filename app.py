from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World from Flask'

if(__name__ == '__main__'):
    app.run(debug=True)


