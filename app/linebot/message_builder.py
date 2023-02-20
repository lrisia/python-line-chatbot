import app.configuration as config

class MessageBuilder():
    """"""

    def __init__(self, message: str) -> None:
        self.message = message

    def build(self) -> dict:
        return {
            "type": "text",
            "text": f"{self.message}"
        }

class ImagemapBuilder(MessageBuilder):
    """"""

    DEFAULT_BASE_SIZE = {
        "width": 1040,
        "height": 1040
    }

    def __init__(self,
        preset: any=None,
        base_url: str="",
        alt_text: str="",
        base_size: dict=DEFAULT_BASE_SIZE,
    ) -> None:
        super().__init__(message=alt_text)
        self.preset = preset
        if not base_url.startswith('/'): base_url = '/' + base_url
        self.base_url = config.server.URL + base_url
        self.base_size = base_size
        self.actions = []

    def build(self) -> dict:
        body = self.preset
        if body: return body
        
        if self.base_url == "" or self.message == "": raise ValueError("Some value was missing.")
        return {
            "type": "imagemap",
            "baseUrl": self.base_url,
            "altText": self.message,
            "baseSize": self.base_size,
            "actions": self.actions
        }

    def add_action(self, type: str="message", area: dict={}, **action: any) -> None:
        try:
            temp = area["x"]
            temp = area["y"]
            temp = area["width"]
            temp = area["height"]
        except:
            raise ValueError("Some value was missing.")

        if type == "message":
            try: text = action["text"]
            except: raise ValueError("Some value was missing.")
            self.actions.append({
                "type": type,
                "area": area,
                "text": text
            })

class ImageBuilder(MessageBuilder):
    """
    """

    def __init__(self, original_content_url: str, preview_image_url: str) -> None:
        if not original_content_url.startswith('/'): original_content_url = '/' + original_content_url
        self.original_content_url = config.server.URL + original_content_url
        if not preview_image_url.startswith('/'): preview_image_url = '/' + preview_image_url
        self.preview_image_url = config.server.URL + preview_image_url

    def build(self) -> dict:
        return {
            "type": "image",
            "originalContentUrl": self.original_content_url,
            "previewImageUrl": self.preview_image_url
        }

class MessageTool:
    """
    """

    def union(self, *messages) -> str:
        temp = [str(message.build()) for message in messages]
        return ','.join(temp)
