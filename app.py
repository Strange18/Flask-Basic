from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os
from flask import request
from flask import jsonify

load_dotenv()

app = Flask(__name__)


def get_connection():
    conn = psycopg2.connect(database=os.getenv('DATABASE_NAME'),
                            user=os.getenv('DATABASE_USER'),
                            password=os.getenv('DATABASE_PASSWORD'),
                            host=os.getenv('DATABASE_HOST'), port="5432")

    return conn


def get_data():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM tbl_student;')
        a = cur.fetchall()
        return a
    except:
        print("Connection not established in get data\n")


insert_query = "INSERT INTO tbl_student (name, roll) VALUES (%s,%s);"


def insert_data(student_name, student_roll):
    try:
        conn = get_connection()
        cur = conn.cursor()
        print(student_name, student_roll)
        cur.execute(insert_query, (student_name, student_roll))
        conn.commit()
        print(conn.Error)
    except:
        print("Data is not inserted into the database")


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    a = get_data()
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        insert_data(name, roll)
        a = get_data()
    return render_template('index.html', data=a)


@app.route('/view', methods=['GET'])
def data():
    a = get_data()
    # return jsonify(a)
    return render_template('view.html', data=a)


if __name__ == '__main__':
    app.run(debug=True)
