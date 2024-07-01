import awsgi

from flask import (Flask,jsonify)

app = Flask(__name__)

def lambda_handler(event, context):
    return {"statusCode": 200, "body": hello_world()}

@app.route('/')
def hello_world():
    return "My Lambda App works"


