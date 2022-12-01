from flask import Flask, render_template, request, jsonify

import psycopg2
import psycopg2.extras
import psycopg2.extensions
import logging
import sys
import json
import requests
import os

app = Flask(__name__)

app.config['DATABASE_URL'] = os.environ['DATABASE_URL']


@app.route('/',methods=['GET'])
def hello_world():  # put application's code here

    connection = psycopg2.connect(app.config["DATABASE_URL"])
    dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        with dict_cur as cursor:
            sql = '''SELECT * FROM buyer
                      '''



            cursor.execute(sql)


            result = cursor.fetchall()
            print(result)
            data = [dict(row) for row in result]

            connection.commit()
    finally:
        connection.close()
    return render_template("index.html", data=data)


@app.route('/items', methods=['GET', 'POST'])
def show_items():  # put application's code here
    data = request.json

    connection = psycopg2.connect(app.config["DATABASE_URL"])
    dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        with dict_cur as cursor:
            sql = '''SELECT * FROM item
                      '''

            cursor.execute(sql, )

            result = cursor.fetchall()
            print(result)
            data = [dict(row) for row in result]


            connection.commit()
    finally:
        connection.close()
    return render_template("items.html", data=data)

@app.route('/bids', methods=['GET', 'POST'])
def show_bids():  # put application's code here
    data = request.json

    connection = psycopg2.connect(app.config["DATABASE_URL"])
    dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        with dict_cur as cursor:
            sql = '''SELECT * FROM bid
                      '''

            cursor.execute(sql, )

            result = cursor.fetchall()
            print(result)

            connection.commit()
    finally:
        connection.close()
    return render_template("bids.html", data=jsonify(result))


if __name__ == '__main__':
    app.run()
