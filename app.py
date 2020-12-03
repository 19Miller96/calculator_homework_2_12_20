from flask import Flask

app = Flask(__name__)
from modules import calculator

if __name__ == '__main__':
    app.run(debug=True)

    