from flask import Flask, request,  send_from_directory, render_template

import core

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook = core.Webhook(request.json)
    model = core.Model()
    # if เป็นรูป message ให้ทำ message builder แล้วส่งให้ webhook reply กลับไป
    # พรุ่งนี้ค่อยทำไปนอนละ

@app.route('/images/<dirname>/<size>', methods=['GET'])
def get_image(dirname, size):
    return send_from_directory('', path='')