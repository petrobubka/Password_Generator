from flask import Flask, redirect, url_for, request, render_template, make_response

import requests
import string
import random

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')



@app.route('/password', methods=['POST', 'GET'])
def generate():
        if request.method == 'POST':
            inp = int(request.form['nm'])
            digits = string.digits
            punctuation = string.punctuation
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            lenght = inp // 4
            a = random.choices(string.digits, k=lenght)
            b = random.choices(string.punctuation, k=lenght)
            c = random.choices(string.ascii_uppercase, k=lenght)
            d = random.choices(string.ascii_lowercase, k=(inp - (inp // 4 * 3)))
            result = a + b + c + d
            random.shuffle(result)
            password = "".join(result)
            return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run()



