from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)

def get_user_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SSTI Challenge</title>
        </head>
        <body>
            <h1>Welcome to the SSTI Challenge!</h1>
            <form action="/greet" method="get">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name">
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    template = f'Hello {{ {name} }}!'
    return render_template_string(template, get_user_file=get_user_file)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=4000)
