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
    name = request.args.get('name', 'World')
    template = f'Hello {{ {name} }}!'
    return render_template_string(template, get_user_file=get_user_file)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=4000)
