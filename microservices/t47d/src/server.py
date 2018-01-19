from src import app
import requests
from flask import jsonify, render_template, request, make_response,json

@app.route("/")
def home():
    return "Hasura Hello World"

# Uncomment to add a new URL at /new

@app.route("/json")
def json_message():
    return jsonify(message="Hello World")

@app.route("/index")
def index():
    return render_template('dlogin.html')

@app.route("/regdisplay", methods = ['POST', 'GET'])
def registerpage():
    return render_template('dregister.html')

@app.route("/dlogin", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        vuser = request.form['hvName']
        vpwd = request.form['hvPwd']
    # This is the url to which the query is made
    url = "https://auth.anthology78.hasura-app.io/v1/login"

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": vuser,
            "password": vpwd
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }
    print(requestPayload)
    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.

    print(resp.content)
    return (render_template('homedrive.html',name = vuser,msg = resp.content))


@app.route("/dregister", methods = ['POST', 'GET'])
def dregister():

    # This is the url to which the query is made
    url = "https://auth.anthology78.hasura-app.io/v1/signup"

    vuser = request.form['hvName']
    vpwd = request.form['hvPwd']
    # This is the json payload for the query
    requestPayload = {
    "provider": "username",
    "data": {
        "username": vuser,
        "password": vpwd
            }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    #  resp.content contains the json response.
    print (resp.content)
    return render_template('dlogin.html')

# Handling all other request and robots.txt request
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404