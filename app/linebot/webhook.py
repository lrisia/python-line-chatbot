import configuration as config

from core.file_handle import FileHandle
from linebot.message_builder import MessageBuilder

class Webhook:
    """Handle post request from line webhook"""

    DEFAULT_LINE_API = "https://api.line.me/v2/bot/message/reply"

    def __init__(self, payload: str) -> None:
        """__init__ method
        
        Args:
            payload: payload from line webhook
        """
        
        self.file_handle = FileHandle()
        try:
            events = payload['events'][0]
            self.userId = events['source']['userId']
            self.message = events['message']['text'].strip().lower()
            self.reply_token = events['replyToken']
        except Exception as e:
            self.file_handle.write_error(e=e)
        self.header = {
            'Content-Type': 'application/json', 
            'Authorization': 'Bearer {%s}'%config.line_api.CHANNEL_ACCESS_TOKEN
        }

    def reply_message(self, reply_token: str, message: MessageBuilder,) -> None:
        pass