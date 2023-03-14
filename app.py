from flask import Flask, redirect, url_for, request, render_template, make_response
import requests
import string
import random
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="Passwords",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/password', methods=['POST', 'GET'])
def generate():
        if request.method == 'POST':
            inp = int(request.form['nm'])
            lenght = inp // 4
            a = random.choices(string.digits, k=lenght)
            b = random.choices(string.punctuation, k=lenght)
            c = random.choices(string.ascii_uppercase, k=lenght)
            d = random.choices(string.ascii_lowercase, k=(inp - (inp // 4 * 3)))
            result = a + b + c + d
            random.shuffle(result)
            password = "".join(result)
            cur.execute("INSERT INTO passwords (passvalues) VALUES (%s)", (password,))
            conn.commit()

            return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run()



