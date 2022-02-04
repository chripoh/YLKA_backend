from ast import arg
from dataclasses import field
import email
from tokenize import String
from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal
from user import User

app = Flask(__name__)
api = Api(app)

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=String, help='Email-Adress of user')
user_parser.add_argument('name', type=String, help='Name of user')
user_parser.add_argument('password', type=String, help='Password of user')


class User(Resource):
    def get(self):
        return {'a': 100, 'b': 'foo'}

    def post(self):
        args = user_parser.parse_args()
        name=user_parser['name']
        password=user_parser['password']
        email=user_parser['email']
        u1 = User(
            name=name, password=password, email=email)
        u1.create()
        return 'data'


api.add_resource(User, '/user',)  # /user Endpoint for YLKA-Backend


if __name__ == '__main__':
    app.run()  # runs Flask Server
