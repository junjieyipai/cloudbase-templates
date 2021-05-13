
import os

import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return random.randint(1, 55)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
