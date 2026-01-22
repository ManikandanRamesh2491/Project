from flask import Flask, send_from_directory, request, jsonify
import aws_lambda_wsgi

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

def lambda_handler(event, context):
    return aws_lambda_wsgi.response(app, event, context)