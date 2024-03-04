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

    if response:
        return jsonify(response)
    else:
        return jsonify({'error': 'Failed to fetch GraphQL data'})

@app.route("/problem")
def get_match_problem():
    client = graphqlClient()
    cookie1 = {'session': '''ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218960c02ca73c3-0f3fc749555cb-13462c6c-1fa400-18960c02ca81b34%22%2C%22%24device_id%22%3A%2218960c02ca73c3-0f3fc749555cb-13462c6c-1fa400-18960c02ca81b34%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; __stripe_mid=91be8981-b70a-4757-acbd-cf6c0df6967beb4397; csrftoken=I7HmiGbRFPCEj9rVda5uo5JnXJ65AVnhFOZkCmTSN4MgQG1lhNZ7NFPa9gx0mPGB; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTMzMTM1NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImY4ODU0NjYzMGUzZmRjNjRiOWI1MTQyMzQ4ZmYzMjhlNTU4NGE4NDliYzM0M2EyZDhiYWFjYzQ0OWE2ZDg1ZTIiLCJpZCI6NTMzMTM1NSwiZW1haWwiOiJkaGlyYWpib21tYUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6IkRoaXJhakItMTIzIiwidXNlcl9zbHVnIjoiRGhpcmFqQi0xMjMiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY3ODE1MzI0Mi5wbmciLCJyZWZyZXNoZWRfYXQiOjE3MDk0MzI3NDUsImlwIjoiMjYwMTo2NDY6YTI4MTo4ZDA2OjhjNjk6M2IyNTpmN2U4OmNjMzUiLCJpZGVudGl0eSI6ImRmMzA3Njg5MmNjZDAxNDdjYTZlMGVmNDY3MzU5NWQwIiwic2Vzc2lvbl9pZCI6NTE5MjAyMjF9.ODJhq5r5WcuEm5RKLrBbhb5U1VMJmLLofGdEuospT0g; _dd_s=rum=0&expire=1709433649137; INGRESSCOOKIE=8432e7228b24d5f51d51972eae64aa65|8e0876c7c1464cc0ac96bc2edceabd27'''}
    response = client.get_match_problem(cookie1, cookie1, "", [])
    if response:
        return jsonify(response)
    else:
        return jsonify({'error': 'Failed to fetch GraphQL data'})

if __name__ == "__main__":
    socketio.run(app, debug=True)
