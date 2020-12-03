from app import app
from modules import calculator

@app.route('/+')
def add():
    return f"this equals {int(num1) + int(num2)}

@app.route('/-')
def subtract():
    return f"this equals {int(num1) - int(num2)} 

@app.route('/*')
def multiply():
    return f"this equals {int(num1) - int(num2)}

@app.route('//')
def divide():
    return f"this equals {int(num1) - int(num2)}
