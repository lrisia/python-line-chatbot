from flask import Flask, render_template, request, send_from_directory
# from core import *
from core.file_handle import FileHandle

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
    f = FileHandle()
    f.write_log(conf=0.8, answer="abcdefghijklmnopqrstuvwxyz")
    f.write_error(error="File not found", cause="File does't exits")

if __name__ == '__main__':
    main()
