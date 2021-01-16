from flask import Flask, jsonify
import os

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return jsonify({'message': 'Hi'})

    @app.route('/Bye')
    def bye():
        return jsonify({'message': 'Bye'})

    return app