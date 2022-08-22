from glob import escape
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<company>/employees")
def employed(company):
    with open(f'../db/{company}.emp', 'a+') as file:
        file.seek(0, 0)
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

@app.route("/<company>/employees/<name>")
def addEmployee(company, name):
    with open(f'../db/{company}.emp', 'a+') as file:
        file.write(f'{name}\n')
    return f'Adding {name} as an employee'

@app.route("/<company>/employees/fire/<name>")
def fireEmployee(company, name):
    with open(f'../db/{company}.emp', 'a+') as file:
        file.seek(0, 0)
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    lines.remove(f'{name}')
    with open(f'../db/{company}.emp', 'w') as file:
        file.writelines(f'{emp}\n' for emp in lines)
    return f'You just fired {name} from {company}'