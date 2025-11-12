from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, I'm under the water, here too much raining.'
