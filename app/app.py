from flask import Flask, request,  send_from_directory, render_template

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json

@app.route('/images/<dirname>/<size>', methods=['GET'])
def get_image(dirname, size):
    return send_from_directory('', path='')

