from flask import Flask, redirect, url_for, request, render_template, make_response
import requests
import string
import random
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin123",
    host="passwords.chwbwjv5imju.eu-north-1.rds.amazonaws.com",
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

@app.route('/all_passwords')
def all_passwords():
    cur.execute("SELECT passvalues FROM passwords")
    passwords = cur.fetchall()
    return render_template('all_passwords.html', passwords=passwords)

@app.route('/delete', methods=['POST'])
def delete_all_passwords():
    cur.execute("DELETE FROM passwords")
    conn.commit()
    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run()



