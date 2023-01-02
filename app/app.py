from flask import Flask, request,  send_from_directory, render_template

from models import *

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
def webhook():
    # webhook = Webhook(request.json)
    model = Model()
    # if เป็นรูป message ให้ทำ message builder แล้วส่งให้ webhook reply กลับไป
    # พรุ่งนี้ค่อยทำไปนอนละ

# @app.route('/images/<dirname>/<size>', methods=['GET'])
# def get_image(dirname, size):
#     return send_from_directory('', path='')

if __name__ == '__main__':
    webhook()