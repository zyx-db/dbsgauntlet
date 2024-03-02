import json
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit, join_room, close_room
from graphql import *
import requests

from graphql.query import graphqlClient

app = Flask(__name__)
# TODO make real secret key
app.config["SECRET_KEY"] = 'db_rocks'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    print('client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('client disconnected')

@socketio.on('join')
def handle_message(data):
    print("join_room")

@socketio.on('leave')
def leave_room(data):
    print("leave room")

def generate_problem():
    return "hello"

def validate_submission():
    pass

@app.route('/graphql', methods = ["POST"])
def graphql():
    client = graphqlClient()
    problem = request.form["problem"]
    cookie = {"session": request.form["cookie"]}
    response = client.get_problem_status(problem, cookie)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch GraphQL data'}), response.status_code

def rand_prob():
    graphql_endpoint = 'https://leetcode.com/graphql/'
    query = '''
        query randomQuestion($categorySlug: String, $filters: QuestionListFilterInput) {
          randomQuestion(categorySlug: $categorySlug, filters: $filters) {
            titleSlug
          }
        }
'''
    variables = {
            'categorySlug': 'all-code-essentials',
            'filters': {
                'difficulty': 'MEDIUM',
                'tags': ['array']
                }
            }
    response = requests.post(graphql_endpoint, json={'query': query, 'variables': variables})
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch GraphQL data'}), response.status_code

if __name__ == "__main__":
    socketio.run(app)
