class Webhook:
    """Handle post request from line webhook"""

    def __init__(self, payload: str) -> None:
        """__init__ method
        
        Args:
            payload: payload from line webhook
        """

        self.events = payload['events'][0]
        self.userId = self.events['source']['userId']
        self.message = self.events['message']['text'].strip().lower()
        self.reply_token = self.events['replyToken']

    def reply(self):
        pass