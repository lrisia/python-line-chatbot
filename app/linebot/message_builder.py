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
        actions: list=list()
    ) -> None:
        self.preset = preset
        self.base_url = base_url
        self.alt_text = alt_text
        self.base_size = base_size
        self.actions = actions
        print(type(actions))
        print(type(self.actions))

    def build(self) -> dict:
        body = self.preset
        if body: return body
        
        if self.base_url == "" or self.alt_text == "": raise ValueError("Some value was missing.")
        return {
            "type": "imagemap",
            "baseUrl": self.base_url,
            "altText": self.alt_text,
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
