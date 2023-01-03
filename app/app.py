from flask import Flask, render_template, request, send_from_directory
from core import *
from linebot import *

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     webhook = Webhook(request.json)
#     model = Model()
#     # if เป็นรูป message ให้ทำ message builder แล้วส่งให้ webhook reply กลับไป
#     # พรุ่งนี้ค่อยทำไปนอนละ

# @app.route('/images/<dirname>/<size>', methods=['GET'])
# def get_image(dirname, size):
#     return send_from_directory('', path='')

def main():
    m = ImagemapBuilder(base_url="base_url", alt_text="alt_text", actions={"type": "message",})
    # m.add_action(area={
    #       "x": 529,
    #       "y": 411,
    #       "width": 497,
    #       "height": 120
    #     }, text="ขั้นตอนที่ 3")
    # print(m.build())

if __name__ == '__main__':
    main()
