from flask import Flask, render_template, request, send_from_directory
from app.core import *
from app.linebot import *

app = Flask(__name__)

model = Model()

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook = Webhook(request.json)
    answer = model.predict(text=webhook.get_message())
    webhook.reply_message("", MessageBuilder(answer).build())
    return []
    # if เป็นรูป message ให้ทำ message builder แล้วส่งให้ webhook reply กลับไป
    # พรุ่งนี้ค่อยทำไปนอนละ

@app.route('/images/<dirname>/<size>', methods=['GET'])
def get_image(dirname, size):
    return send_from_directory('', path='')

def fetch():
    global model
    model = Model()


# def main():
#     m = Model()
#     print(m.predict(text="วิธีการบันทึกข้อมูลแผนพัฒนา"))

# if __name__ == '__main__':
#     main()
