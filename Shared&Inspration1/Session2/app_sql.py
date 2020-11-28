from flask import (Flask, abort, jsonify, request)
from flask_cors import CORS
import os
from sqlalchemy import create_engine, text

import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

customer = pd.read_json('customers.json')
# engine=create_engine(conn_info, echo=False)


password = os.getenv('POSTGRES_PASSWORD')
conn_info = 'postgresql://postgres:{}@localhost:5432/test'.format("______")
engine = create_engine(conn_info, echo=False)


@app.route("/")
def hello():
    return "Share & Inspire Lab!"


@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    stmt = "select id, name, age, gender, email from customer where id=:id"
    result = engine.execute(text(stmt), id=customer_id).fetchall()
    result_dict = [dict(row) for row in result]
    return jsonify(result_dict[0])


# @app.route('/customer/age/<int:age>', methods=["GET"])
# def get_customer_by_age(age):
#     df=customer[['age'] == age]
#     df.to_json()
#

@app.route('/customers', methods=["POST"])
def search_customers():
    try:
        if request.method == "POST":
            content = request.json
            name = content['name']
            name = "%" + name + "%"
            stmt = "select id, name, age, gender, email from customer where name like :name"
            result = engine.execute(text(stmt), name=name).fetchall()
            return jsonify({'customer': [dict(row) for row in result]})
        else:
            abort([501, "input text required"])
    except IndexError:
        abort(404)
